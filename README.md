# Rootly Incident MCP Server

A simple MCP server that fetches incident data from the Rootly API.

## Setup

1. Create a virtual environment (recommended):
> Install uv if not present `curl -LsSf https://astral.sh/uv/install.sh | sh
`
```bash
uv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

2. Install dependencies:
```bash
uv install
```

3. Create a `.env` file in the root directory with your Rootly API key:
```
cp .env.example .env # modify the file after copying
```
4. Add to your Editor/Client of choice
Some examples are below
* Sample config for cursor is [here][.cursor/mcp.json]
* Follow instructions at bottom of [this mcp tutorial](https://modelcontextprotocol.io/quickstart/server) for claude desktop

> Include paths to the executable with the commands names in these json files. Use `which < command name >` to find paths

## Running the Server



## Debugging
Use the MCP instructor by running the node command
```
npx @modelcontextprotocol/inspector
```
To start the server for debugging, run:

```bash
python src/mcp_server.py
```

## Features


## Error Handling


## Requirements

- Python 3.12+
- See requirements.txt for package dependencies 