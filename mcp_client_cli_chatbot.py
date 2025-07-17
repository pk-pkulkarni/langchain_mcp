#!/usr/bin/env python3
import asyncio
import os
from dotenv import load_dotenv

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI


def _setup_environment():
    # Load environment variables from .env file
    load_dotenv()
    # Ensure OPENAI_API_KEY is available
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise EnvironmentError("OPENAI_API_KEY not set in environment or .env file.")
    os.environ["OPENAI_API_KEY"] = key


async def main():
    # Prepare environment
    _setup_environment()

    # Initialize MultiServerMCPClient with configured MCP endpoints
    client = MultiServerMCPClient(
        {
            "restaurant": {
                "url": "http://localhost:3900/mcp",
                "transport": "streamable_http",
            }
            # You can add more MCP servers here with the same structure.
        }
    )

    # Fetch available tools from the MCP server(s)
    tools = await client.get_tools()

    # Create Chat model
    model = ChatOpenAI(model="gpt-4o")

    # Build a ReAct-style agent with retrieved tools
    agent = create_react_agent(model, tools)

    # CLI loop
    print("MCO Client CLI Chatbot (type 'exit' or Ctrl+C to quit)")
    while True:
        try:
            user_input = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input.strip():
            continue
        if user_input.lower().strip() in ("exit", "quit"):
            print("Goodbye!")
            break

        # Wrap user message in the messages format
        payload = {"messages": [{"role": "user", "content": user_input} ]}

        # Invoke the agent asynchronously and retrieve response
        try:
            result = await agent.ainvoke(payload)
            bot_reply = result["messages"][-1].content
        except Exception as e:
            bot_reply = f"Error during agent invocation: {e}"

        print(f"Bot: {bot_reply}\n")


if __name__ == "__main__":
    asyncio.run(main())
