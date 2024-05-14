import requests
from get_token import get_token
from get_building_sectors import get_building_sector_id, get_building_sectors
from get_alarm_sectors import get_alarm_sectors, get_alarm_sector_id
from get_alarm_types import get_alarm_types, get_brand_alarm_type_id

def post_alarm(session_token, alarm_type_id, alarm_sector_id, building_sector_id):
    url = "https://tas01.evalarm.de/api/v1/alarms"
    headers = {
        "x-evalarm-api-session": session_token,
        "x-evalarm-api-version": "2.1.3"
    }
    data = {
        "alarm": {
            "message": "Testalarm",
            "building_sectors": [building_sector_id],
            "room_sectors": [],
            "alarm_sectors": [alarm_sector_id],
            "kind": "building",
            "alarm_type": alarm_type_id,
            "alarm_levels": [],
            "alarm_intensity": 2,
            "espa_system_id": "1",
            "espa_detector_group": "",
            "espa_detector_id": "",
            "current_status": 1
        }
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

building_sectors = get_building_sectors(get_token())
building_sector_id = get_building_sector_id(building_sectors, "Werk 1")

alarm_sectors = get_alarm_sectors(get_token())
alarm_sector_id = get_alarm_sector_id(alarm_sectors, "Halle 1 - Lager")

alarm_types = get_alarm_types(get_token())
alarm_type_id = get_brand_alarm_type_id(alarm_types)

print(post_alarm(get_token(), alarm_type_id, alarm_sector_id, building_sector_id))