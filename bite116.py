import os

ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    files = os.listdir(dirname)
    files_filtered = [x for x in files if os.path.getsize(f'{dirname}/{x}') >= ONE_KB*size_in_kb]
    return files_filtered

print(get_files('temp', 1000))