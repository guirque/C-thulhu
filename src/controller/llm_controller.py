import model.llm as model 
from model.tools.toolkit import folder_data

def invoke(prompt, current_path="/"):
    """
        Invokes the llm and returns its content.
    """
    folder_data.set_current_folder(current_path)
    return model.invoke_llm(prompt)

def api_key_exists():
    return model.google_api_key is not None

def update_api_key(value):
    model.update_api_key(value)