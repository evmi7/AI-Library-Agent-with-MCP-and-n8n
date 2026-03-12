# AI Library Agent (MCP + n8n)

AI agent pro vyhledávání knih v osobní knihovně exportované z **Calibre**.  
Projekt demonstruje použití **LLM agenta**, **Model Context Protocol (MCP)** a **workflow nástroje n8n**.

Agent dokáže odpovídat na dotazy typu:

- Find books by Woody Allen
- Find book Nadace
- Search books by author

a vrátí strukturovaný seznam knih.

---

# Project Architecture

System architecture:

User  
↓  
LLM Agent (ReAct)  
↓  
MCP Server (Python)  
↓  
Tool: `search_books`  
↓  
n8n Webhook API  
↓  
Workflow `api_search_books`  
↓  
Workflow `search_calibre_book`  
↓  
Calibre CSV dataset  

---

# Technologies Used

- Python
- Model Context Protocol (MCP)
- OpenAI Agents SDK
- n8n
- HTTP API
- CSV dataset (Calibre export)

---

# Architecture Diagram

```mermaid
flowchart TD

User["User Question"]
Agent["LLM Agent (ReAct)"]
MCP["MCP Server (Python)"]
Tool["Tool: search_books"]
Webhook["n8n Webhook"]
Wrapper["Workflow: api_search_books"]
SearchWF["Workflow: search_calibre_book"]
CSV["Calibre CSV Dataset"]

User --> Agent
Agent --> MCP
MCP --> Tool
Tool --> Webhook
Webhook --> Wrapper
Wrapper --> SearchWF
SearchWF --> CSV
CSV --> SearchWF
SearchWF --> Wrapper
Wrapper --> MCP
MCP --> Agent
Agent --> User
