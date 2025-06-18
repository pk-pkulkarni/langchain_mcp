# LangChain MCP – Restaurant Example

A demonstration of using **Model Context Protocol (MCP)** to expose a restaurant interaction tool that integrates with LangChain.

---

## 📁 Repo Structure

- `restaurant_mcp.py` – MCP server exposing restaurant-related tools.
- `restaurant_data.py` – Mock dataset (restaurant listings and menus).
- `mcp_client.py` – Python client to connect and call MCP server tools.
- `requirements.txt` – Python dependencies for server & client.
- `.env` – Environment variables files, will have you OPENAI_API_KEY

---

## 🚀 Setup

1. **Clone and install dependencies**

   ```bash
   git clone https://github.com/pk-pkulkarni/langchain_mcp.git
   cd langchain_mcp
   pip install -r requirements.txt

2. **Run the MCP server**
  Open a terminal and start the server:
   ```bash
   python restaurant_mcp.py
⚠️ *Make sure `restaurant_mcp.py` is running as a server* in your terminal before proceeding.

3. **Run the client**  
In a separate terminal, run:
```bash
python mcp_client.py
