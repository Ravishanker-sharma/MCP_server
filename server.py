from typing import Any
import httpx
import datetime
from mcp.server.fastmcp import FastMCP
from genralscraper import get_data
from fastscraper import scraper
from googlecal import calendar_details, list_events, create_event ,Event

mcp = FastMCP("SearchEngine")

@mcp.tool()
async def search(query: str) -> Any:
    """
    This tool is used to perform web search and retrieve data.
    :param query: string
    :return: any
    """
    return await get_data(query)

@mcp.tool()
async def scrape(url: list) -> Any:
    """
    This function can be used to scrape a list of urls.
    :param url: list
    :return: any
    """
    try:
        return await scraper(url)
    except Exception as e:
        return f"Error occurred: {e}"

@mcp.tool()
async def get_current_time() -> str:
    """
    This function returns the current date, time and day.
    :return: string
    """
    try:
        current_datetime = datetime.datetime.now()
        friendly_format = current_datetime.strftime("%A, %B %d, %Y at %I:%M %p")
        return friendly_format
    except Exception as e:
        return f"Error occurred: {e}"

@mcp.tool()
async def get_calendar_events(time,maxresults):
    """
        This function lists the upcoming events on your calendar.
        :param time: Needs a time in ISO format. For example: 2023-01-01T00:00:00Z.
        :param maxresults: Number of events to be returned. For example: 10.
        :return: list of events.
    """
    try:
        events = list_events(time,maxresults)
        return events
    except Exception as e:
        return f"Error occurred: {e}"

@mcp.tool()
async def create_event_in_calendar(event)-> str:
    '''
        This function creates an event on your calendar.
        Example Input Schema:
            """
Example Input Schema:
{
    "summary": "Test Event",
    "location": "800 Howard St., San Francisco, CA 94103",
    "description": "A chance to hear more about Google's developer products.",
    "start": {
        "dateTime": "2025-08-07T11:00:00+05:30",
        "timeZone": "Asia/Kolkata"
    },
    "end": {
        "dateTime": "2025-08-07T12:00:00+05:30",
        "timeZone": "Asia/Kolkata"
    },
    "attendees": [
        {"email": "lpage@example.com"},
        {"email": "sbrin@example.com"}
    ],
    "reminders": {
        "useDefault": false,
        "overrides": [
            {"method": "email", "minutes": 1440},
            {"method": "popup", "minutes": 10}
        ]
    }
}
"""
        :param event: Event object.
        :return: String containing the link to the event.
    '''
    try:
        return create_event(event)
    except Exception as e:
        return f"Error occurred: {e}"

@mcp.tool()
async def get_calendar_details():
    """"
        This function returns the details of your calendar.
    """
    try:
        return calendar_details()
    except Exception as e:
        return f"Error occurred: {e}"


if __name__ == "__main__":
    mcp.run(transport="stdio")