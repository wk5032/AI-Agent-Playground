from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession
import asyncio
import sys


async def connect_to_streamble_server(server_url: str):
    # Connect to a streamable HTTP server
    async with streamablehttp_client(url=server_url) as (
        read_stream,
        write_stream,
        _,
    ):
        # Create a session using the client streams
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()
            # List available tools
            tools = await session.list_tools()
            print("Tools:", tools)

            # call a tool
            score = await session.call_tool(name="get_score_by_name",arguments={"name": "张三"})

            print("score: ", score)

             # List available resources
            resources = await session.list_resources()

            # Read a resource
            content, mime_type = await session.read_resource("file://info.md")

            print("resource: ", mime_type)

            # List available prompts
            prompts = await session.list_prompts()

            # Get a prompt
            prompt = await session.get_prompt(
                "prompt", arguments={"name": "张三"}
            )

            print("prompt: ", prompt) 

async def main():
    if len(sys.argv) < 2:
        print("Usage: uv run client.py <URL of Streamble HTTP MCP server (i.e. http://localhost:8000/mcp)>")
        sys.exit(1)
    
    await connect_to_streamble_server(server_url=sys.argv[1])

if __name__ == "__main__":
    asyncio.run(main())