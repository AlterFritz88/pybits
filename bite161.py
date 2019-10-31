import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    dir = 0
    file = 0
    for root, dirs, files in os.walk('venv'):
        file += len(files)
        dir += len(dirs)
    return dir, file

print(count_dirs_and_files())

