
# Architektura systému

Projekt využívá AI agenta, který komunikuje s nástrojem pomocí Model Context Protocol.

## Komponenty

1. AI Agent (ReAct)
2. MCP Server (Python)
3. n8n workflow
4. CSV dataset knih

## Tok dat

User → Agent → MCP → n8n Webhook → Workflow → CSV databáze → odpověď JSON
