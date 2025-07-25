import os
import tempfile

class FileController:
    """Controller responsible for file management"""
    
    def __init__(self):
        pass

    def process_file(self, file):
        """Process a single file"""

        # Directory where the files will be saved
        save_dir = os.path.join(tempfile.gettempdir(), "uploaded_files")
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # Save the file in the directory
        file_path = os.path.join(save_dir, file.name)
        with open(file_path, "wb") as f:
            f.write(file.read())

        # Return information about the saved file
        return {"name": file.name, "path": file_path}


    def process_multiple_files(self, files):    
        """Process multiple files"""
        return [self.process_file(file) for file in files]

    def clear_all_files(self):
        """Clear all files"""
        clear_dir = os.path.join(tempfile.gettempdir(), "uploaded_files")
        if os.path.exists(clear_dir):
            for file in os.listdir(clear_dir):
                os.remove(os.path.join(clear_dir, file))
        return True