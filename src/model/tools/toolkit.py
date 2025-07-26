from langchain_core.tools import tool
from glob import glob
import os

# Utils --------------------------------------------------------------------------------------------------------

def get_content(path):
    return glob(os.path.join(path, "*"))

# Folder Data --------------------------------------------------------------------------------------------------

class FolderData:
    current_folder = "/"

    def set_current_folder(self, folderpath: str):
        """
            Use this function to set the current folder being analyzed (``current_folder``). All other function (tools) will work with the specified folder.
            Returns True if the folder was found. False, otherwise.
        """
        if len(get_content(folderpath)) > 0:
            self.current_folder = folderpath
            return True
        else:
            return False

folder_data = FolderData()

# Tools --------------------------------------------------------------------------------------------------------

"""
Tool ideas
- set_current_folder(folderpath)
- open_file(filename)
- write_file(filename, content, erase_content=False)
- list_folder_content(folder_name)
- move_file
"""

@tool
def list_folder_content(folderpath: str):
    """
        Use this function to list content of a specific folder, inside ``current_folder``. Use "." for the content inside the ``current_folder``.
        Returns an array of file and folder names, found inside "folderpath".
    """

    return glob(os.path.join(folder_data.current_folder, folderpath, "**")) if folderpath != "." else get_content(folder_data.current_folder)

tookit = [list_folder_content]