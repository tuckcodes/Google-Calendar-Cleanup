from __future__ import print_function

# Code speed test stuff
import time
t0 = time.perf_counter()

import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import timedelta


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.events']
        
def deleteEvent(event, service):
    _eventId = str(event['id'])
    service.events().delete(calendarId='<YOUREMAILHERE>', eventId=_eventId).execute()
        

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
            
        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Retreiving the calendar events...')
        events_result = service.events().list(
            calendarId='<YOUREMAILHERE>', 
            timeMin=now,
            maxResults=10, # Change this number to retrive more total results 
            singleEvents=False, # Leave as false to only retreive the parent of reoccuring events 
            showDeleted=False,
            q='<CUSTOM QUERY STRING GOES HERE>'
            # orderBy='startTime',
            ).execute()
        
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        counter = 0
        for event in events:
            counter += 1
            if event['status'] != "cancelled":
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, event['summary'], counter)
        

            
        userDecision = input("Do you want to delete all of these emails? 'Yes' or 'No': ")

        while (userDecision != "Yes") and (userDecision != "No"):
            userDecision = input("Please answer with Yes or No to confirm: ")

        if userDecision == "Yes":
            counter = 0      
            for event in events:
                deleteEvent(event, service)
                counter += 1
                print("#" + str(counter) + " | Deleted " + event['summary'] + " | id:(" + event['id'] + ")")
        elif userDecision == "No":
            print("Adios!")
            exit()
        else:
            exit()

        # Code speed test stuff
        t1 = time.perf_counter()
        speed = (t1-t0)
        print("Completed! Execution time was ", speed)

    except HttpError as error:
        print('An error occurred: %s' % error)



if __name__ == '__main__':
    main()
    
    
