import pandas as pd
from RawData.enums import ColumnEnum
from RawData.models import RawData

def _parse_date(val):
    try:
        result = pd.to_datetime(int(val), unit='D', origin='1899-12-30')
    except Exception:
        result = pd.to_datetime(val, dayfirst=True, errors='coerce')
    return None if pd.isnull(result) else result.date()


def _prepare_data(load_file, df_records):
    return [RawData(
        file=load_file,
        **{col.value.lower(): record[col.value] for col in ColumnEnum}
    ) for record in df_records]


def _normalize_columns(df_records):
    rename_map = {col: col for col in df_records.columns}
    expected = {col.value.lower(): col.value for col in ColumnEnum}
    for actual_col in df_records.columns:
        lower = actual_col.lower()
        if lower in expected:
            rename_map[actual_col] = expected[lower]
    df_records = df_records.rename(columns=rename_map)

    missing = [col.value for col in ColumnEnum if col.value not in df_records.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")
    return df_records


def _normalize_data(df_records):
    df_records = _normalize_columns(df_records)
    start = ColumnEnum.START.value
    end = ColumnEnum.END.value

    df_records[start] = df_records[start].apply(_parse_date)
    df_records[end] = df_records[end].apply(_parse_date)
    return df_records

def _convert_data(df_records):
    return df_records.to_dict('records')

def insert_data_to_db(load_file , df_records):
    df_records = _normalize_data(df_records)
    df_records_dict = _convert_data(df_records)
    model_instances = _prepare_data(load_file , df_records_dict)
    RawData.objects.bulk_create(model_instances)