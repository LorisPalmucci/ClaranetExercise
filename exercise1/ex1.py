import os
import sys

def replace_in_file(file_path, old_str, new_str):
    with open(file_path, 'r') as f:
        file_content = f.read()
    file_content = file_content.replace(old_str, new_str)
    with open(file_path, 'w') as f:
        f.write(file_content)

def replace_in_directory(dir_path, old_str, new_str):
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            replace_in_file(file_path, old_str, new_str)

if __name__ == '__main__':
    old_str = sys.argv[1]
    new_str = sys.argv[2]
    dir_path = sys.argv[3]
    replace_in_directory(dir_path, old_str, new_str)