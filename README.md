# AI Library Agent with MCP and n8n

Agent pro vyhledávání knih v osobní knihovně (Calibre export CSV) pomocí **LLM agenta**, **MCP serveru** a **n8n workflow**.

Projekt demonstruje architekturu:

LLM Agent  
↓  
MCP Server (Python)  
↓  
Tool: `search_books`  
↓  
n8n Webhook API  
↓  
Workflow `search_calibre_book`  
↓  
Calibre CSV dataset  

Agent dokáže odpovídat na dotazy typu:

- Najdi knihy od Woody Allen
- Najdi knihu Nadace

a vrátí strukturovaný seznam knih.

---

# Použitá architektura

Projekt využívá:

**Agent pattern**

ReAct agent

Agent používá nástroje (tools) dostupné přes **MCP server**.

---

# Použité technologie

- Python
- Model Context Protocol (MCP)
- OpenAI Agents SDK
- n8n workflow automation
- Calibre export (CSV databáze knih)
- PowerShell / HTTP API testování

---

# Architektura systému

User  
↓  
AI Agent  
↓  
MCP Server (Python)  
↓  
Tool: search_books  
↓  
HTTP POST  
↓  
n8n Webhook  
↓  
Workflow api_search_books  
↓  
Workflow search_calibre_book  
↓  
CSV knihovna  

---

# MCP Tool

Agent má k dispozici tool: search_books(query, limit)

Příklad volání:

```json
{
  "query": "Woody Allen",
  "limit": 5
}

n8n workflow

Projekt obsahuje dva workflow:
1) api_search_books
2) API wrapper workflow.

Webhook
↓
Edit Fields
↓
Execute Workflow (search_calibre_book)
↓
Code
↓
Respond to Webhook
search_calibre_book

Interní workflow pro vyhledávání knih v CSV.

When Executed by Another Workflow
↓
Set_query
↓
Read CSV File
↓
Extract from CSV
↓
CodeJS_ALL1in1 (filtrace)
Datový zdroj

Knihovna je exportovaná z Calibre do CSV.
CSV obsahuje pole:
Nazev
Autor
Knihovna

Workflow filtruje data podle:
Nazev
Autor

API odpověď
API vrací JSON:

{
  "status": "ok",
  "query": "Woody Allen",
  "count": 1,
  "results": [
    {
      "id": "bk_1",
      "title": "Velký šéf a další povídky",
      "author": "Woody Allen",
      "library": "Calibre AUDIO"
    }
  ]
}

Instalace
1️⃣ Python prostředí
python -m venv .venv
Aktivace:
Windows
.venv\Scripts\activate
2️⃣ instalace balíčků
pip install mcp
pip install httpx
pip install uvicorn
Spuštění MCP serveru
python server.py

Server poskytuje MCP tool:
search_books

který volá n8n webhook.
n8n konfigurace

Webhook endpoint:
POST http://localhost:5678/webhook/search_books

Workflow musí být:
Activate / Publish
Test API

Test z PowerShellu:
Invoke-RestMethod -Method Post `
  -Uri "http://localhost:5678/webhook/search_books" `
  -ContentType "application/json" `
  -Body '{"query":"Woody Allen","limit":5}'
Ukázka odpovědi
status query       count
------ -----       -----
ok     Woody Allen     1
Implementace vyhledávání

Vyhledávání používá jednoduchý filtr:
nazev.includes(query)
autor.includes(query)
Dotaz je normalizován na lowercase.

Možná rozšíření
Projekt lze rozšířit o:
fuzzy vyhledávání autorů
vyhledávání podle série
vyhledávání audioknih
transkripce videí
doporučování knih
vector search (embeddingy)

Struktura repozitáře
calibre-mcp-agent/
│
├─ server.py
├─ agent_main.py
├─ requirements.txt
│
├─ workflows/
│   ├─ api_search_books.json
│   └─ search_calibre_book.json
│
├─ data/
│   └─ calibre_books.csv
│
└─ README.md

Projekt splňuje požadavky zadání:
Agent:
ReAct agent

Framework:
OpenAI Agents SDK

Tools:
Custom MCP tool
n8n workflow
CSV databáze
Autor
Projekt vytvořil:
Evmi: pro účely výuky a experimentů s AI agenty.
Licence: MIT License

✅ Tento soubor můžeš:
- uložit jako **README.md**
- commitnout do GitHubu
- GitHub ho automaticky zobrazí jako dokumentaci projektu.
