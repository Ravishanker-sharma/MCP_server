### GENERAL MCP Server

---

#### Project Structure and Components

The project consists of several Python scripts that work together to create a web scraping and calendar management server using `FastMCP`.

* **`.gitignore`**: This file specifies files and directories that should be ignored by Git, such as byte-compiled files, IDE-specific settings (`.idea/`, `*.iml`), environment folders (`venv/`, `env/`), and log files.

* **`yahoosearchengine.py`**:
    * **Purpose**: Implements a custom Yahoo search client.
    * **Key Functions**:
        * `extract_real_url(yahoo_url)`: Decodes and extracts the actual URL from a Yahoo search result link.
        * `yahoo_search(query)`: Performs a search on Yahoo and returns a list of URLs from the results.

* **`genralscraper.py`**:
    * **Purpose**: A multithreaded web scraper that uses `yahoosearchengine.py` to get URLs and then scrapes content from them.
    * **Key Functions**:
        * `extract_image_url(soup, domain)`: Extracts image URLs for specific domains like `hindustantimes.com` and `indianexpress.com`.
        * `smart_scrape(url, section=None)`: Scrapes headlines, paragraphs, and images from a given URL using `BeautifulSoup` and a rotating list of user agents.
        * `get_data(querry)`: The main function that orchestrates the search and scraping process, using threads for parallel scraping.

* **`fastscraper.py`**:
    * **Purpose**: An asynchronous web scraper that uses the `crawl4ai` library for high-speed scraping.
    * **Key Functions**:
        * `scraper(urls)`: An `async` function that scrapes a list of URLs concurrently and extracts data based on a predefined CSS schema for headlines, paragraphs, and article blocks.

* **`googlecal.py`**:
    * **Purpose**: Provides functions for interacting with the Google Calendar API.
    * **Dependencies**: Requires `pydantic` for data validation, `google.auth`, and `google-api-python-client`.
    * **Key Functions**:
        * `calendar_details()`: Retrieves details of the primary calendar.
        * `list_events(time, maxresults)`: Fetches a list of upcoming calendar events.
        * `create_event(event)`: Creates a new event in the calendar.

* **`server.py`**:
    * **Purpose**: The main server application built with `FastMCP`, which exposes the project's functionalities as tools.
    * **Exposed Tools**:
        * `search(query: str)`: Performs a web search and scrapes content using `fastscraper.py`.
        * `get_current_time()`: Returns the current date and time.
        * `get_calendar_events(time, maxresults)`: Lists events from Google Calendar.
        * `create_event_in_calendar(event)`: Creates a new calendar event.
        * `get_calendar_details()`: Retrieves calendar details.

---

### Getting Started

To run this project, you will need to install the necessary Python dependencies and configure Google Calendar API credentials.

**1. Install Dependencies**:

```bash
pip install requests beautifulsoup4 crawl4ai fastmcp google-api-python-client google-auth-oauthlib pydantic langchain
