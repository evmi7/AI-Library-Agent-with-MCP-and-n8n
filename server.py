
from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP("calibre-library-agent")

N8N_URL = "http://localhost:5678/webhook/search_books"

@mcp.tool()
async def search_books(query: str, limit: int = 5):
    payload = {
        "query": query,
        "limit": limit
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(N8N_URL, json=payload)

    return response.json()

if __name__ == "__main__":
    mcp.run()
