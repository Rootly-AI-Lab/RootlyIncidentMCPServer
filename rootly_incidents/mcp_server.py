from mcp.server.fastmcp import FastMCP
import httpx
from typing import Any
import os
import dotenv   

# Get the parent directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Load .env from parent directory
dotenv_path = os.path.join(parent_dir, '.env')
if not os.path.exists(dotenv_path):
    raise FileNotFoundError(f"Required .env file not found at {dotenv_path}. Please create one based on .env.example")

dotenv.load_dotenv(dotenv_path)

if not os.getenv('ROOTLY_API_KEY'):
    raise ValueError("ROOTLY_API_KEY is not set in the .env file")


mcp = FastMCP("rootly")
INCIDENT_URL = "https://api.rootly.com/v1/incidents"

@mcp.tool()
async def get_rootly_incidents() -> list[dict[str, str]]:
    """
    Get recent incidents from Rootly
    """
    return await get_rootly_incidents_from_api()

async def get_rootly_incidents_from_api() -> list[dict[str, str]]:
    """
    Get recent incidents from Rootly API
    """
    headers = {
        "Authorization": f"Bearer {os.getenv('ROOTLY_API_KEY')}"
    }
    querystring = {
        "page[size]":"10"
        # Add more filters
        }


    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(INCIDENT_URL, headers=headers, params=querystring, timeout=30.0)
            response.raise_for_status()
            return get_incident_titles(response.json())
        except Exception:
            return {"error": "Failed to get incidents from Rootly"}

def get_incident_titles(incidents: dict[str, Any]) -> list[str]:
    """
    Get incident titles from Rootly
    """
    try:
        incidents = incidents["data"]
        return [
            {
                "title": incident["attributes"]["title"],
                "id": incident["id"],
                "status": incident["attributes"]["status"],
                "created_at": incident["attributes"]["created_at"],
                "updated_at": incident["attributes"]["updated_at"]
                # Add more fields
            } for incident in incidents]
    except KeyError:
        return []
    

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')