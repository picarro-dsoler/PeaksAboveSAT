from gasanalytics.box import *
from boxsdk import Client
from boxsdk.object.folder import Folder
from pathlib import Path
import warnings
class BoxFolder:
    def __init__(self, parent_folder_id = None):
        self.id = None
        if parent_folder_id is None:
            raise ValueError('Parent folder id is required')
        self.parent_folder_id = parent_folder_id
        self.subfolders = []
    def get_subfolders(self):
        for item in client.folder(folder_id=str(self.parent_folder_id)).get_items():
            if item.type == "folder":
                self.subfolders.append(item)
        return self.subfolders

    def find_folder(self, folder_name):
        self.get_subfolders()
        for item in self.subfolders:
            if item.name == folder_name:
                return item
        return None

    def create_folder(self, folder_name):
        try:
            self.box_obj = create_subfolder(self.parent_folder_id, self.name)
            self.id = self.box_obj.id
        except Exception as e:
            print(f'Error creating folder {self.name}')
            folder_items = get_item_ids_in_folder(self.parent_folder_id)
            for key, value in folder_items.items():
                if key == self.name:
                    self.id = value
                    print(f'Folder {self.name} found in parent folder {self.parent_folder_id}')
                    break
            if self.id is None:
                raise ValueError(f'Folder {self.name} not found in parent folder {self.parent_folder_id}')


