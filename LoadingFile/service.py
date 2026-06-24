from io import BytesIO
import pandas as pd
from LoadingFile.models import LoadFile
from LoadingFile.utils import get_file_hash

def read_file(file):
    if not file.name.lower().endswith(('.xls', '.xlsx')):
        raise ValueError("Only XLS/XLSX files are supported")
    file_bytes = BytesIO(file.read())
    return pd.read_excel(file_bytes), file_bytes

def check_exist_file(file_bytes):
    file_hash = get_file_hash(file_bytes)
    return LoadFile.objects.filter(file_hash=file_hash).first(), file_hash

def create_file(file_name, file_hash, user):
    return LoadFile.objects.create(
        file_name=file_name,
        file_hash=file_hash,
        user=user,
    )
