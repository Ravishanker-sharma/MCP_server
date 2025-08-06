from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
from genralscraper import get_data
from fastscraper import scraper
from yahoosearchengine import yahoo_search

mcp = FastMCP("SearchEngine")

@mcp.tool()
async def search(query: str) -> Any:
    """
    This tool is used to perform web search and retrieve data.
    :param query: string
    :return: any
    """
    return await scraper(yahoo_search(query))

if __name__ == "__main__":
    mcp.run(transport="stdio")