#!/usr/bin/env python3
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

# Load environment variables
def _setup_env():
    load_dotenv()
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise EnvironmentError("OPENAI_API_KEY not set in .env or environment")
    os.environ["OPENAI_API_KEY"] = key

_setup_env()

# FastAPI application
app = FastAPI(
    title="MCP Client Chatbot API",
    description="Expose your MCP-powered ReAct agent via HTTP",
)
# Enable CORS for any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request and response models
class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    answer: str

# Globals for client and agent
client: MultiServerMCPClient | None = None
agent: any = None

# Configure and create MCP client
def _create_client() -> MultiServerMCPClient:
    return MultiServerMCPClient({
        "restaurant": {
            "url": "http://localhost:3900/mcp",
            "transport": "streamable_http",
        }
    })

# Startup: initialize client, tools, model, agent
@app.on_event("startup")
async def startup_event():
    global client, agent
    client = _create_client()
    tools = await client.get_tools()
    model = ChatOpenAI(model="gpt-4o")
    agent = create_react_agent(model, tools)

# Health check endpoint
@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok"}

# Chat endpoint matching frontend's {query: q} format
@app.post("/chat", response_model=QueryResponse, tags=["Chat"])
async def chat_endpoint(req: QueryRequest):
    global agent
    if agent is None:
        raise HTTPException(status_code=503, detail="Agent not ready")

    payload = {"messages": [{"role": "user", "content": req.query}]}
    try:
        result = await agent.ainvoke(payload)
        # Extract latest assistant message
        messages = result.get("messages", [])
        answer = messages[-1].content if messages else ""
        return QueryResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent error: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("mcp_client_api_chatbot:app", host="0.0.0.0", port=8000, reload=True)


# uvicorn mcp_client_api_chatbot:app --reload --port 8000