import requests
from get_token import get_token

def get_alarm_sectors(session_token):
    url = "https://tas01.evalarm.de/api/v1/alarm_sectors"
    headers = {
        "x-evalarm-api-session": session_token,
        "x-evalarm-api-version": "2.1.3"
    }
    response = requests.get(url, headers=headers)
    return response.json()

def get_alarm_sector_id(alarm_sectors, alarm_sector_name):
    for alarm_sector in alarm_sectors["alarm_sectors"]:
        if alarm_sector["name"] == alarm_sector_name:
            return alarm_sector["id"]