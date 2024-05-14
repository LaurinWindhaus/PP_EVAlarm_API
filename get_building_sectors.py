import requests
from get_token import get_token

def get_building_sectors(session_token):
    url = "https://tas01.evalarm.de/api/v1/building_sectors"
    headers = {
        "x-evalarm-api-session": session_token,
        "x-evalarm-api-version": "2.1.3"
    }
    response = requests.get(url, headers=headers)
    return response.json()

def get_building_sector_id(building_sectors, building_sector_name):
    for building_sector in building_sectors["building_sectors"]:
        if building_sector["name"] == building_sector_name:
            return building_sector["id"]