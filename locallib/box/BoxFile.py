from dotenv import load_dotenv
load_dotenv(override=True)

from gasanalytics.box import *
from pathlib import Path
import warnings

class BoxFile:
    def __init__(self, local_path = None, box_folder_id = None, box_file_id = None):
        self.local_path = Path(local_path)
        
        self.box_folder_id = box_folder_id
        self.box_file_id = box_file_id

        #Check that the file exists locally
        if not self.local_path.exists():
            warnings.warn(f'The file {self.local_path.as_posix()} does not exist locally')

        self.name = self.local_path.name

        #Check that there is either a file id or a folder id
        if (box_file_id is None) & (box_folder_id is None):
            raise ValueError('Either file_id or folder_id is required')

        #If the file_id is not there, get it from the folder
        if (box_file_id is None):
            self.box_file_id = self.get_file_id_in_folder()

    def download(self):
        if self.box_file_id is not None:
            #Download the new file
            download_file(self.box_file_id, self.local_path.as_posix())
        else:
            raise ValueError('No remote file found, check the file id or the folder id')

    def get_item_id_in_folder(self):
        return get_item_ids_in_folder(self.box_folder_id)
    
    def get_file_id_in_folder(self):
        try:
            return get_item_ids_in_folder(self.box_folder_id)[self.name]
        except:
            return None

    def upload(self):
        if self.box_file_id is None:
            f = upload_new_file(self.box_folder_id, self.local_path.as_posix(), self.name)
            self.box_file_id = f.id
        else:
            update_file_with_new_version(self.box_file_id, self.local_path.as_posix())

    def delete(self, site = 'local'):
        if site == 'local':
            #Delete the local file
            self.local_path.unlink()
        elif site == 'box':
            delete_file(self.box_file_id)
        else:
            raise ValueError('Invalid site, must be local or box')


class BoxFile_old:
    def __init__(self, local_path = None, box_folder_id = None, box_file_id = None):

        #The constructor needs a local file path and a box folder id or a box file id
        if local_path is not None:
            if box_folder_id is not None:
                #Get the file id if exists
                self.local_path = Path(local_path)
                self.name = self.local_path.name
                self.box_folder_id = box_folder_id
                #Get the file id if exists
                try:
                    self.box_file_id = get_item_ids_in_folder(self.box_folder_id)[self.local_path.as_posix()]
                except:
                    self.box_file_id = None
            else:
                raise ValueError('box_folder_id is required')

        elif box_file_id is not None:
            #Get the file object
            self.box_file_id = box_file_id
            self.file_obj = get_file_object(self.box_file_id)

            #Get the file name
            self.name = self.file_obj.name

            #Create the tmp directory
            self.tmp_dir = Path(f'tmp_{self.box_file_id}')
            self.tmp_dir.mkdir(exist_ok=True)

            #Download the file
            self.local_path = Path(f'{self.tmp_dir / self.name}')
            download_file(self.box_file_id, self.local_path)

    def getFilePath(self):
        return self.local_path

    def delete_temp_file(self):
        #if temp folder exists delete it
        if self.tmp_dir.exists():
            self.tmp_dir.rmdir()

    


