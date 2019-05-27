import os

path, dirs, files = next(os.walk("E:\\desktop\\lab python\\python-learning-space\\tempfile\\tempfile"))
file_count = len(files)

print(file_count)