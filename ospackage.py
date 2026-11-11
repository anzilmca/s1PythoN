import os

print(os.getcwd())

path = os.path.expanduser("~/Desktop/Python/osmodule")

os.chdir(path)

print(os.getcwd())
