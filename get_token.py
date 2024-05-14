import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_token():
    url = "https://tas01.evalarm.de/api/v1/sessions"
    payload = {
        "namespace": os.getenv('NAMESPACE'),
        "email": os.getenv('EMAIL'),
        "password": os.getenv('PASSWORD'),
        "bearer": os.getenv('BEARER')
    }
    headers = {
        "Content-Type": "application/json",
        "x-evalarm-api-version": "2.1.3"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()["session"]

print(get_token())