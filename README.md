# gcalcleanup
### An easily modified Google Calendar Cleanup tool that can be ran locally via terminal

> Note: The script will show you the results, and then ask you to proceed with deletion. It does NOT delete without permission first.

- [Create a project on GCP](https://console.cloud.google.com/projectcreate) if you don't have one already
- You will likely need to [enable the Calendar API](https://console.cloud.google.com/apis/library/calendar-json.googleapis.com) for that project
- Create an "Desktop App" [OAtuh credential on GCP](https://console.cloud.google.com/apis/credentials/oauthclient)
- Click the JSON export button
<img width="385" alt="image" src="https://user-images.githubusercontent.com/18519239/169217613-c2d89324-09a8-4056-a35b-fb33a30b9fe6.png">
- Save as 'credentials.json' into your local repo 
  <img width="130" alt="image" src="https://user-images.githubusercontent.com/18519239/169217778-8372a2ca-6e54-4868-b732-87a720bf2fba.png">
- Modify the following lines
https://github.com/tuckcodes/Google-Calendar-Cleanup/blob/e2b4e49392a16a828514066c4e989336e1895555/gcalcleanup.py#L22

https://github.com/tuckcodes/Google-Calendar-Cleanup/blob/e2b4e49392a16a828514066c4e989336e1895555/gcalcleanup.py#L55

https://github.com/tuckcodes/Google-Calendar-Cleanup/blob/e2b4e49392a16a828514066c4e989336e1895555/gcalcleanup.py#L57

https://github.com/tuckcodes/Google-Calendar-Cleanup/blob/e2b4e49392a16a828514066c4e989336e1895555/gcalcleanup.py#L60

- Run the following
``` python
python gcalcleanup.py
```

- The script will auto-generate a token.json file. If you are iterating with this script, sometimes you need to delete it as it stores scoping/permissions stuff and can hinder expected outcomes with code changes.

A successful run looks like this:
<img width="1096" alt="Screenshot 2022-05-18 233222" src="https://user-images.githubusercontent.com/18519239/169220950-18189831-0c5a-4113-aa28-4e6f4c11870e.png">


## Notes
If you have python errors, make sure you have python3 installed. If PATH isnt set, you can also try running:
``` python
python3 gcalcleanup.py
```

## Things that can improve
- [ ] Concurrent API calls
> The script currently churns out about 1 call per second, or 60 per minute, due to its sequential nature. For smaler loads this may not be an issue, but some folks like myself may be dealing with thousands of events. The Google API quota is about 240 per minute limit, which means this could see a 3x or 4x increase in throughput with concurrent calls. 
