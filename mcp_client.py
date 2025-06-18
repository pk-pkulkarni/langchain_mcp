from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

import asyncio


async def main():
    client = MultiServerMCPClient(
        {
            "restaurant": {
                "url": "http://localhost:3900/mcp",  # Ensure server is running here
                "transport": "streamable_http",
            }
            # Add another MCP server if you want
            # "furniture": {
            #     "url": "http://localhost:3800/mcp",
            #     "transport": "streamable_http",
            # }

        }
    )

    import os
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

    tools = await client.get_tools()
    model = ChatOpenAI(model="gpt-4o")
    agent = create_react_agent(
        model, tools
    )

    restaurant_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "Get veg menu for Spice Garden restaurant?"}]}
    )
    print("Restaurant response:", restaurant_response['messages'][-1].content)


asyncio.run(main())
