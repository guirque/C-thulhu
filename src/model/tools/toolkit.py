from langchain_core.tools import tool
from glob import glob
from streamlit.logger import get_logger
import os

LOGGER = get_logger(__name__)

# Utils --------------------------------------------------------------------------------------------------------

def get_content(path, recursive=False):
    return glob(os.path.join(path, "**"), recursive=recursive)

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
def list_folder_content(folderpath: str, recursive=False):
    """
        Use this function to list content of a specific folder, inside ``current_folder``. Use "." for the content inside the ``current_folder``.
        Use ``recursive=True`` if you need to see content inside of folders.
        Returns an array of file and folder names, found inside "folderpath".
    """

    LOGGER.info(f"model called tool list_folder_content({folderpath}, {recursive})")

    return glob(os.path.join(folder_data.current_folder, folderpath, "**"), recursive=recursive) if folderpath != "." else get_content(folder_data.current_folder, recursive=recursive)


@tool
def move_file(filepath: str, destination: str):
    """
        Use this function to move or rename a file inside ``current_folder``. "filepath" is the path including the file name starting from ``current_folder``.
        "destination" is the path including the new file name, starting from ``current_folder``.
        Returns True on success and an object with an error message, otherwise.
    """

    LOGGER.info(f"model called tool move_file({filepath}, {destination})")

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

    LOGGER.info(f"model called tool write_to_file({filename}, {content})")

    filepath = os.path.join(folder_data.current_folder, filename)
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

    LOGGER.info(f"model called tool read_file({filepath})")

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

@tool
def make_item(filepath: str, type: str, content=None):
    """
        Use this function to create a file or folder inside ``current_folder``. ``filepath`` must include the file or folder name.
        ``type`` must be either "file" or "folder". ``content`` is optional and can be used to insert content into the created file.
        Returns True on success and an object with an error message, otherwise.
    """

    LOGGER.info(f"model called tool make_item({filepath}, {type}, {content})")

    try:
        path = os.path.join(folder_data.current_folder, filepath)

        if type == "folder":
            os.mkdir(path)
        else:
            with open(path, "w") as file:
                if content is not None:
                    file.write(content)
    except:
        return {
            "Error": "Could not create or open file or folder. This could happen if a path is invalid or due to permission errors."
        }


tookit = [list_folder_content, move_file, write_to_file, read_file, make_item]