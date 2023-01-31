from os import chdir
from glob import glob


def list_files(path):
    return glob(path + "/*")
