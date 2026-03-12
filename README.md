# AI knihovní agent (MCP + n8n)

Tento projekt demonstruje vytvoření **AI agenta**, který dokáže vyhledávat knihy v osobní knihovně exportované z aplikace **Calibre**.

Agent využívá:

- **Model Context Protocol (MCP)** pro přístup k nástrojům
- **OpenAI Agents SDK**
- **n8n workflow** jako backend pro zpracování dat
- **CSV databázi knih** exportovanou z Calibre

Agent dokáže odpovídat na dotazy typu:

- Najdi knihy od Woody Allen
- Najdi knihu Nadace
- Najdi knihy podle autora

a vrací strukturovaný seznam knih.

---

# Architektura systému

Architektura řešení:

Uživatel  
↓  
LLM Agent (ReAct)  
↓  
MCP Server (Python)  
↓  
Nástroj: `search_books`  
↓  
n8n Webhook API  
↓  
Workflow `api_search_books`  
↓  
Workflow `search_calibre_book`  
↓  
CSV databáze knih  

---

# Použité technologie

Projekt využívá následující technologie:

- Python
- Model Context Protocol (MCP)
- OpenAI Agents SDK
- n8n (workflow automatizace)
- HTTP API
- CSV dataset (export z Calibre)

---

# Diagram architektury

```mermaid
flowchart TD

User["Dotaz uživatele"]
Agent["LLM Agent (ReAct)"]
MCP["MCP Server (Python)"]
Tool["Tool: search_books"]
Webhook["n8n Webhook"]
Wrapper["Workflow: api_search_books"]
SearchWF["Workflow: search_calibre_book"]
CSV["CSV databáze Calibre"]

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
