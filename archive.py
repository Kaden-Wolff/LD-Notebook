import os
from collections import defaultdict
from datetime import date
import shutil


# Class object that can hold a file's path and contents, as well as provides a method for returning
# the contents of the file with a header and footer
class TextFile:
    def __init__(self, file_name, directory):
        self.file_name = file_name
        self.directory = directory
        self.file_path = directory + os.sep + file_name

    def return_file(self):
        return open(self.file_path, 'r')

    def return_text(self):
        return open(self.file_path, 'r').read()

    def insert_file(self):
        return ('----------{file_path}----------'
                '\n'
                '{file_text}'
                '\n'
                '----------{file_path}----------'
                '\n').format(file_path=self.file_path, file_text=self.return_text())

    def __repr__(self):
        return 'file at : ' + self.file_path


# Generates a timestamped directory path to place today's files in.
def today_archive_path(directory):
    dir_name = date.today().isoformat().replace('-', '')
    path = directory + os.sep + dir_name
    return path


# Moves all files from one directory to another.
def move_files(source_dir, target_dir):
    file_names = os.listdir(source_dir)

    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)


# Copies all files from one directory to another.
def copy_files(source_dir, target_dir):
    file_names = os.listdir(source_dir)

    for file_name in file_names:
        shutil.copy(os.path.join(source_dir, file_name), target_dir)


# Walks through all subdirectories of a directory and returns an object with the files within grouped by name.
def extract_directory(directory):
    compiled_files = defaultdict(list)
    for directory, subdirs, files in os.walk(directory, topdown=True):
        for file_name in files:
            file = TextFile(file_name, directory)
            compiled_files[file.file_name].append(file)
    return compiled_files


# Writes all files to the specified directory
def write_files(compiled_files, directory):
    for file_name, files in compiled_files.items():
        file_contents = [file.insert_file() for file in files]
        text = '\n'.join(file_contents)
        file = open(directory + os.sep + file_name, "w")
        file.write(text)
        file.close()


if __name__ == '__main__':
    today_path = today_archive_path('daily archive')
    try:
        os.mkdir(today_path)
    except FileExistsError as e:
        raise e
    move_files('today', today_path)
    move_files('tomorrow', 'today')
    copy_files('template', 'tomorrow')
    compiled_files = extract_directory('daily archive')
    write_files(compiled_files, 'archive compiled')
