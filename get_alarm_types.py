import requests
from get_token import get_token

def get_alarm_types(session_token):
    url = "https://tas01.evalarm.de/api/v1/alarm_types"
    headers = {
        "x-evalarm-api-session": session_token,
        "x-evalarm-api-version": "2.1.3"
    }
    response = requests.get(url, headers=headers)
    return response.json()

def get_brand_alarm_type_id(alarm_types):
    for alarm_type in alarm_types["alarm_types"]:
        if alarm_type["name"]["de"] == "Brand":
            return alarm_type["id"]