import requests
from config import AppConfigs

import base64
import json

USERNAME = AppConfigs().GITEA_USERNAME
PASSWORD = AppConfigs().GITEA_PASSWORD

def get_data():
    url = f"https://git.de-cloak.com/api/v1/users/{USERNAME}/activities/feeds?limit=5&date=2024-01-29"

    basic_auth = base64.b64encode(f"{USERNAME}:{PASSWORD}".encode()).decode()
    print(basic_auth)

    payload = {}
    headers = {
        'Authorization': f'Basic {basic_auth}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)

    print(len(response.json()))
    content = response.json()[0]["content"]
    # print(content)

    # transform the content to json
    content = json.loads(content)
    print(content)
    print(content["Commits"][0]["Sha1"])
    print(content["Commits"][0]["Message"])
    print(content["Commits"][0]["Timestamp"])
    print(content["CompareURL"])

    # print(json.dumps(content, indent=4, sort_keys=True))


if __name__ == "__main__":
    get_data()
    
