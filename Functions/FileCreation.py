
import os

class FileCreation:
    
    @staticmethod
    def create_textfile(folder_path: str, file_name: str):
        file_path = f'{folder_path}/{file_name}'
        if os.path.exists(file_path) and os.path.isfile(file_path):
            print(f'File: {file_path} already exists')
            return file_path
        else:
            file = open(file_path, "w")
            file.close()
            if os.path.exists(file_path) and os.path.isfile(file_path):
                print(f'File: {file_path} created successfully')
                return file_path
            else:
                raise Exception(f'Failed to create file: {file_path}')