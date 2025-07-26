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
- read_file(filename)
- write_file(filename, content, erase_content=False)
- list_folder_content(folder_name)
- move_file(filename, destination)
"""

@tool
def list_folder_content(folderpath: str):
    """
        Use this function to list content of a specific folder, inside ``current_folder``. Use "." for the content inside the ``current_folder``.
        Returns an array of file and folder names, found inside "folderpath".
    """

    return glob(os.path.join(folder_data.current_folder, folderpath, "**")) if folderpath != "." else get_content(folder_data.current_folder)


@tool
def move_file(filepath: str, destination: str):
    """
        Use this function to move or rename a file inside ``current_folder``. "filepath" is the path including the file name starting from ``current_folder``.
        "destination" is the path including the new file name, starting from ``current_folder``.
        Returns True on success and an object with an error message, otherwise.
    """

    try:
        
        old_path = os.path.join(folder_data.current_folder, filepath)
        new_path = os.path.join(folder_data.current_folder, destination)
        os.rename(old_path, new_path)

    except:
        return {
            "Error": "Could not locate or open file."
        }


@tool
def write_to_file(filename: str, content: str):
    """
        Writes ``content`` to a file with name ``filename`` inside ``current_folder``, returns if successful. Writes over ``filename`` if it already exists inside ``current_folder``.
    """
    print(folder_data.current_folder)
    filepath = os.path.join(folder_data.current_folder, filename)
    print(filepath)
    with open(filepath, "w") as f:
        f.write(content)
        f.flush()
    return f"file {filename} written to {folder_data.current_folder}"


@tool
def read_file(filepath: str):
    """
        Use this function to read the content of a file inside ``current_folder``.
        Returns the a content on success and an object with an error message, otherwise.
    """
    try:   

        path = os.path.join(folder_data.current_folder, filepath)
        content = None
        with open(path, "r") as file:
            content = file.read()
        return content

    except:
        return {
            "Error": "Could not locate or open file."
        }

tookit = [list_folder_content, move_file, write_to_file, read_file]