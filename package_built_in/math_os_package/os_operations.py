import os

def current_directory():
    return os.getcwd()

def list_files():
    return os.listdir()

def create_folder(name):
    os.mkdir(name)
