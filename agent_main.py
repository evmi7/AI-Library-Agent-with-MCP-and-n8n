
from agents import Agent, Runner
from agents.mcp import MCPServerStdio
import asyncio

async def main():

    server = MCPServerStdio(
        command="python",
        args=["server.py"]
    )

    async with server:

        agent = Agent(
            name="Library Agent",
            instructions="""
You are a library assistant.

Use the search_books tool to find books in the library.
If books are found, list them with title and author.
If no books are found, say that no results were found.
""",            mcp_servers=[server]
        )

        result = await Runner.run(
            agent,
            "Find books by Woody Allen"
        )

        print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
