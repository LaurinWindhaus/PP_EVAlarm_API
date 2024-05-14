import requests
from get_token import get_token

def get_alarms(session_token):
    url = "https://tas01.evalarm.de/api/v1/alarms"
    headers = {
        "x-evalarm-api-session": session_token,
        "x-evalarm-api-version": "2.1.3"
    }
    response = requests.get(url, headers=headers)
    return response.json()

print(get_alarms(get_token()))