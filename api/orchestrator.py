from django.db import transaction

from DataAggregate.service import aggregate_data, insert_aggregated_data
from LoadingFile.models import LoadFile
from LoadingFile.service import read_file, check_exist_file, create_file
from RawData.service import insert_data_to_db


def orchestrator(file_name, file_patch, user):
    df_records, file_bytes = read_file(file_patch)

    existing_file, file_hash = check_exist_file(file_bytes, user)
    if existing_file is not None:
        raise ValueError("File already exists")

    load_file = create_file(file_name=file_name, file_hash=file_hash, user=user)

    try:
        with transaction.atomic():
            insert_data_to_db(load_file, df_records)
            aggregated_data = aggregate_data(load_file)
            insert_aggregated_data(load_file, aggregated_data)
            load_file.file_patch = file_patch
            load_file.loading_status = LoadFile.LoadingFileStatus.Complete
            load_file.save()
    except Exception as e:
        load_file.loading_status = LoadFile.LoadingFileStatus.Error
        load_file.error = str(e)[:256]
        load_file.save()
        raise