
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
│  └─────────────────────────────────────────────────────────────────────────┘ │
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │                        File Controller                                  │ │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────────┐  │ │
│  │  │ process_file()  │  │process_multiple │  │   clear_all_files()     │  │ │
│  │  │                 │  │    _files()     │  │                         │  │ │
│  │  └─────────────────┘  └─────────────────┘  └─────────────────────────┘  │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
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
│  │  │                        read_file()                                  │ │ │
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
│  └─────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Component Description

### 1. **User Interface**  
- **Streamlit Web App**: Interface web interativa com chat, seletor de pastas e input de API key
- **easygui**: Diálogo nativo para seleção de pastas
- **Chat Interface**: Interface de conversação em tempo real com histórico persistente
- **Session State**: Gerenciamento de estado da sessão (folder_path, messages, API key)

### 2. **Agent Core**  
- **Planner**: LangGraph ReAct Agent que quebra tarefas em passos lógicos
- **Executor**: Combina LLM (Gemini 2.5 Flash) com chamadas de ferramentas
- **Memory**: Gerenciamento de estado da sessão e histórico de mensagens

### 3. **Tools / APIs**  
- **Google Gemini API**: LLM principal via langchain_google_genai
- **File Management Tools**: 
  - `list_folder_content()`: Lista conteúdo de pastas usando glob
  - `move_file()`: Move/renomeia arquivos usando os.rename
  - `write_to_file()`: Cria/sobrescreve arquivos com conteúdo
  - `read_file()`: Lê conteúdo de arquivos

### 4. **Observability**  
- **Session State**: Rastreamento de estado da sessão Streamlit
- **Error Handling**: Validação de API key, verificação de pastas, tratamento de erros de operações de arquivo
- **Logging**: Mensagens de chat e respostas do agente preservadas na sessão

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
- API key validation before each operation
- Folder existence verification
- File operation error catching and reporting
- Graceful degradation for missing dependencies

