from langchain_core.tools import tool

# CODE FOR TESTING TOOL CALLING

@tool
def send_message(name: str, message: str):
    """
        Send a message to **name**, with content **message**.
        Returns if the message was sent successfully.
    """
    
    return f"Message sent to {name}: {message} (CONFIRMED)"


@tool
def register_message_sent():
    """
        Register that a message was sent.
        Returns if the message was registered successfully.
    """
    
    return f"Message registered (CONFIRMED)"


tookit = [send_message, register_message_sent]