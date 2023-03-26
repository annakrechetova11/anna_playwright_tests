import os
from json import load


class FileUtils(object):
    def __init__(self):
        self.files_location = "C:\\Users\\annac\\IdeaProjects\\Learning\\files"

    def create_and_read_file(self, string_text, file_name):
        file_path = os.path.join(self.files_location, file_name)
        my_file = open(file_path, 'w')
        my_file.write(string_text)
        my_file.close()
        with open(file_path, 'r') as file_1:
            l = file_1.read()
        return l

    @staticmethod
    def read_json_file(path_to_file):
        with open(os.path.abspath(path_to_file), 'r') as file:
            data = load(file)
        return data
