import datetime
import os.path
from pydantic import BaseModel
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from typing import List, Optional , Dict

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]

class Event(BaseModel):
    summary: str
    location: Optional[str]='Online Event'
    description: str
    start: Dict[str, str]
    end: Dict[str,str]
    attendees: Optional[List[Dict]]
    reminders: Optional[Dict]


try:
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists(r"/Users/ravisharma/PycharmProjects/searchmcp/token.json"):
        creds = Credentials.from_authorized_user_file(r"/Users/ravisharma/PycharmProjects/searchmcp/token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "creds.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("calendar", "v3", credentials=creds)
except Exception as e:
    print("An error occurred: ", e)

def calendar_details():
    """"
    This function returns the details of your calendar.
    """
    try:
        details = service.calendars().get(calendarId="primary").execute()
        return details
    except HttpError as error:
        print(f"An error occurred: {error}")

def list_events(time,maxresults):
    """
    This function lists the upcoming events on your calendar.
    :param time: Needs a time in ISO format. For example: 2023-01-01T00:00:00Z.
    :param maxresults: Number of events to be returned. For example: 10.
    :return: list of events.
    """
    try:
        print("Getting the upcoming 10 events")
        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=time,
                maxResults=maxresults,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])
        return events

    except HttpError as error:
        print(f"An error occurred: {error}")


def create_event(event)-> str:
    """
    This function creates an event on your calendar.
        '''
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
        '''
    :param event: Event object.
    :return: String containing the link to the event.
    """

    event = service.events().insert(calendarId='primary', body=event).execute()
    return event.get('htmlLink')
