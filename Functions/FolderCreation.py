
import os

class FolderCreation:
    
    @staticmethod
    def create_folder(folder_name: str):
        temp = os.path.expanduser('~/Documents')
        temp = temp.replace("\\", "/").replace("Documents", folder_name)
        if os.path.exists(temp):
            print(f'Folder: {temp} already exists')
            return temp
        else:
            os.mkdir(temp)
            if os.path.exists(temp):
                print(f'Folder: {temp} created successfully')
                return temp
            else:
                raise Exception(f'Failed to create folder: {temp}')