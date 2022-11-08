import os


def check_and_make_dir(path):
    """
    Checks if a directory exists and if not creates it
    :param path: The path to the directory
    :return: None
    """
    if not os.path.exists(path):
        os.mkdir(path)
