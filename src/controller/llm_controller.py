import model.llm as model 

def invoke(prompt):
    """
        Invokes the llm and returns its content.
    """
    return model.model.invoke(prompt)

def api_key_exists():
    return model.google_api_key is not None

def update_api_key(value):
    model.update_api_key(value)