import hashlib


def get_file_hash(file) -> str:
    file.seek(0)
    result = hashlib.md5(file.read()).hexdigest()
    file.seek(0)
    return result
