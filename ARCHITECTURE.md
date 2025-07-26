
# ASCII Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              USER INTERFACE                                  │
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │                           Streamlit Web App                             │ │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────────┐  │ │
│  │  │   Chat Input    │  │  Folder Picker  │  │    API Key Input        │  │ │
│  │  │                 │  │   (easygui)     │  │                         │  │ │
│  │  └─────────────────┘  └─────────────────┘  └─────────────────────────┘  │ │
│  │  ┌─────────────────────────────────────────────────────────────────────┐ │ │
│  │  │                    Session State Management                         │ │ │
│  │  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────┐  │ │ │
│  │  │  │  folder_path    │  │    messages     │  │    API Key Storage  │  │ │ │
│  │  │  └─────────────────┘  └─────────────────┘  └─────────────────────┘  │ │ │
│  │  └─────────────────────────────────────────────────────────────────────┘ │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              CONTROLLER LAYER                               │
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │                        LLM Controller                                   │ │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────────┐  │ │
│  │  │   invoke()      │  │ api_key_exists()│  │   update_api_key()      │  │ │
│  │  │ (messages, path)│  │                 │  │                         │  │ │
│  │  └─────────────────┘  └─────────────────┘  └─────────────────────────┘  │ │
│  └─────────────────────────────────────────────────────────────────────────┘ ││
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              AGENT CORE                                      │
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │                           LLM Model                                      │ │
│  │  ┌─────────────────────────────────────────────────────────────────────┐ │ │
│  │  │              Google Gemini 2.5 Flash                                 │ │ │
│  │  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────┐  │ │ │
│  │  │  │  create_model() │  │  invoke_llm()   │  │  update_api_key()   │  │ │ │
│  │  │  │                 │  │  (messages)     │  │                     │  │ │ │
│  │  │  └─────────────────┘  └─────────────────┘  └─────────────────────┘  │ │ │
│  │  └─────────────────────────────────────────────────────────────────────┘ │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │                        ReAct Agent                                       │ │
│  │  ┌─────────────────────────────────────────────────────────────────────┐ │ │
│  │  │              LangGraph ReAct Agent                                    │ │ │
│  │  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────┐  │ │ │
│  │  │  │    Planner      │  │    Executor     │  │      Memory         │  │ │ │
│  │  │  │  (Task Break-   │  │  (LLM + Tool    │  │   (Session State)   │  │ │ │
│  │  │  │   down)         │  │   Calling)      │  │                     │  │ │ │
│  │  │  └─────────────────┘  └─────────────────┘  └─────────────────────┘  │ │ │
│  │  └─────────────────────────────────────────────────────────────────────┘ │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              TOOLS / APIs                                   │
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │                           File Management Tools                         │ │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────────┐  │ │
│  │  │list_folder_     │  │   move_file()   │  │   write_to_file()       │  │ │
│  │  │content()        │  │                 │  │                         │  │ │
│  │  └─────────────────┘  └─────────────────┘  └─────────────────────────┘  │ │
│  │  ┌─────────────────────────────────────────────────────────────────────┐ │ │
│  │  │                             etc.                                    │ │ │
│  │  └─────────────────────────────────────────────────────────────────────┘ │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │                           Google Gemini API                             │ │
│  │  ┌─────────────────────────────────────────────────────────────────────┐ │ │
│  │  │              langchain_google_genai                                 │ │ │
│  │  │              ChatGoogleGenerativeAI                                 │ │ │
│  │  └─────────────────────────────────────────────────────────────────────┘ │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              OBSERVABILITY                                  │
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │                        Session State Management                         │ │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────────┐  │ │
│  │  │  folder_path    │  │    messages     │  │    API Key Storage      │  │ │
│  │  │                 │  │                 │  │                         │  │ │
│  │  └─────────────────┘  └─────────────────┘  └─────────────────────────┘  │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │                           Error Handling                                │ │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────────┐  │ │
│  │  │  API Key        │  │  Folder         │  │    File Operations      │  │ │
│  │  │  Validation     │  │  Validation     │  │    Error Handling       │  │ │
│  │  └─────────────────┘  └─────────────────┘  └─────────────────────────┘  │ │
│  └─────────────────────────────────────────────────────────────────────────┘
│
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │                           Logging                                       │ │
│  │  ┌─────────────────────────────────────────────────────────────────────┐ │ │
│  │  │                   streamlit.logger                                  │ │ │
│  │  └─────────────────────────────────────────────────────────────────────┘  │
│  └─────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Component Description

### 1. **User Interface**  
- **Streamlit Web App**: Interactive web interface with chat UI, folder selector and API key input.
- **easygui**: Native dialog for folder selection.
- **Chat Interface**: Real-time chat with in-session history.
- **Session State**: Session state management (folder_path, messages, API key)

### 2. **Agent Core**  
- **Planner**: LangGraph ReAct Agent that breaks tasks into logical steps.
- **Executor**: Combination of the LLM Combina LLM (Gemini 2.5 Flash) with tool calling.
- **Memory**: Session state management and chat history.

### 3. **Tools / APIs**  
- **Google Gemini API**: LLM used via langchain_google_genai
- **File Management Tools (implemented functions)**: 
  - `list_folder_content(folderpath)`: Folder content listing using glob
  - `move_file(filepath, destination)`: File movement and renaming using os.rename
  - `write_to_file(filename, content)`: File creation/overwrite with content
  - `read_file(filepath)`: File content reading
  - `make_item(filepath, type)`: File and folder creation.
- **FolderData**: Current folder state management.


### 4. **Observability**  
- **Session State**: Rastreamento de estado da sessão Streamlit
- **Error Handling**: Folder verification and basic error handling.
- **Logging**: Many activities, like tool calling, are logged during runtime and visible on the console. Chat messages are visible during session on the UI.

## Key Implementation Details

### **Data Flow**:
1. **User Input** → Streamlit chat interface
2. **Validation** → API key and folder path validation
3. **Processing** → LLM Controller invokes ReAct Agent
4. **Tool Execution** → File operations via toolkit
5. **Response** → Formatted response back to UI

### **State Management**:
- **folder_path**: Current working directory for file operations
- **messages**: Complete chat history for context
- **API Key**: Dynamic key management for Gemini API

### **Error Handling**:
- API key validation
- Folder existence verification
- File operation error catching and reporting (error message to LLM)

