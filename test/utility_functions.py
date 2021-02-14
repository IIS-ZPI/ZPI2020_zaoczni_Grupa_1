import os


def create_empty_file_in_directory(filename, subdirectory_path):
    directory_path = os.path.join(os.getcwd(), subdirectory_path)
    file_path = os.path.join(os.getcwd(), directory_path, filename)
    if (os.path.exists(directory_path) is False):
        os.mkdir(directory_path)
    if os.path.isfile(file_path):
        os.remove(file_path)
    try:
        open(file_path, "w")
    except IOError:
        return None
    return file_path
