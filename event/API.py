from apiclient.discovery import build
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from datetime import datetime


class GoogleCalendar:

    def sent_to_API(title, start_time1, end_time1):
        credentials = pickle.load(open("token.pkl", "rb"))
        service = build("calendar", "v3", credentials=credentials)
        """"Get my calendar"""
        result = service.calendarList().list().execute()
        calendar_id = result['items'][0]['id']

        """ Create a new event"""

        start_time1 = datetime.strptime(start_time1, "%Y-%m-%d %H:%M:%S")  # convert to datetime
        end_time1 = datetime.strptime(end_time1, "%Y-%m-%d %H:%M:%S")  # convert to datetime
        timezone = 'Europe/Warsaw'

        event = {
            'summary': title,
            'location': 'Warsaw',
            'description': 'Test',
            'start': {
                'dateTime': start_time1.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': timezone,
            },
            'end': {
                'dateTime': end_time1.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': timezone,
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
        service.events().insert(calendarId=calendar_id, body=event).execute()

    def edit_to_API(title, start_time1, end_time1, event_id):
        credentials = pickle.load(open("token.pkl", "rb"))
        service = build("calendar", "v3", credentials=credentials)
        result = service.calendarList().list().execute()
        calendar_id = result['items'][0]['id']
        timezone = 'Europe/Warsaw'
        event = {
            'summary': title,
            'location': 'Warsaw',
            'description': 'Test',
            'start': {
                'dateTime': start_time1.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': timezone,
            },
            'end': {
                'dateTime': end_time1.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': timezone,
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
        service.events().update(calendarId=calendar_id, eventId=event_id, body=event).execute()

    def get_event_id():
        """ This function return google calendar event id as string - last value from table"""
        credentials = pickle.load(open("token.pkl", "rb"))
        service = build("calendar", "v3", credentials=credentials)
        result = service.calendarList().list().execute()
        calendar_id = result['items'][0]['id']
        result = service.events().list(calendarId=calendar_id, maxResults=2400).execute()
        table_size = len(result['items'])
        event_id = result['items'][table_size - 1]['id']
        return event_id

    def delete_from_API(event_id):
        credentials = pickle.load(open("token.pkl", "rb"))
        service = build("calendar", "v3", credentials=credentials)
        result = service.calendarList().list().execute()
        calendar_id = result['items'][0]['id']
        service.events().delete(calendarId=calendar_id, eventId=event_id).execute()

