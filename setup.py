import json

import requests

# Konfigurasi
ip = "192.168.1.108"
url = f"http://{ip}/RPC2"

payload = {
    "method": "configManager.setConfig",
    "params": {
        "name": "EventHttpUpload",
        "table": {
            "Enable": True,
            "Type": "digest",
            "UploadServerList": [
                {
                    "Address": "example.com",
                    "AuthEnable": False,
                    "EventType": ["AccessControl", "DoorStatus"],
                    "HttpsEnable": False,
                    "Password": "",
                    "Port": 80,
                    "Uploadpath": "/",
                    "UserName": "",
                }
            ],
        },
    },
    "id": 1000,
    "session": "",
}

headers = {"Content-Type": "application/json"}

try:
    response = requests.post(url, headers=headers, json=payload, timeout=10)

    print("HTTP Status:", response.status_code)
    print("Response:")
    print(json.dumps(response.json(), indent=4))

except requests.exceptions.RequestException as e:
    print("Error:", e)
