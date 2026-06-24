import pandas as pd

from DataAggregate.models import AggregateData
from RawData.models import RawData


def insert_aggregated_data(load_file, aggregated_data):
    instances = [
        AggregateData(
            load_file=load_file,
            group_by_value=row['start_year'],
            aggregate_value=row['total'],
        )
        for row in aggregated_data
    ]
    AggregateData.objects.bulk_create(instances)


def aggregate_data(file):
    qs = RawData.objects.filter(
        file=file, start__isnull=False, end__isnull=False
    ).values('start', 'end', 'impr')

    df = pd.DataFrame(list(qs))
    if df.empty:
        return []

    df['start'] = pd.to_datetime(df['start'])
    df['end'] = pd.to_datetime(df['end'])
    df['days_total'] = (df['end'] - df['start']).dt.days + 1

    expanded = df.apply(
        lambda r: pd.date_range(r['start'], r['end'])
                    .to_frame(name='date')
                    .assign(impr=r['impr'] / r['days_total']),
        axis=1,
    )
    daily = pd.concat(expanded.tolist())
    daily['year'] = daily['date'].dt.year

    result = (
        daily.groupby('year')['impr']
        .sum()
        .reset_index()
        .rename(columns={'year': 'start_year', 'impr': 'total'})
    )
    return result.to_dict('records')