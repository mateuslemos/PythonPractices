import os 

class FilePath:
    def get_file_path(self, file_name):
        return os.path.join(os.path.dirname(__file__), file_name)