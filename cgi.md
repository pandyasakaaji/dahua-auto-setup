# Dahua RPC2 API Reference

## Authentication

RPC2 endpoints require a session token. CGI endpoints use **Digest Auth**.

### Login (get session token)

```json
POST http://<device-ip>/RPC2

{
    "method": "global.login",
    "params": {
        "userName": "admin",
        "password": "<hashed_password>",
        "clientType": "Web3.0",
        "authorityType": "Default",
        "passwordType": "Default"
    },
    "id": 1
}
```

Response includes `session` token — use it in all subsequent RPC2 requests.

### Digest Auth (CGI endpoints)

CGI endpoints (`/cgi-bin/`) require HTTP Digest Authentication instead of a session token.

```
Authorization: Digest username="admin", realm="...", nonce="...", uri="...", response="..."
```

With curl:
```bash
curl --digest -u admin:<password> "http://<device-ip>/cgi-bin/..."
```

---

## Read Config

### Get Specific

Retrieve a named config entry.

```json
{
    "method": "configManager.getConfig",
    "params": {
        "name": "NTP"
    },
    "id": 999,
    "session": "<session_token>"
}
```

### Get All

List all available config names.

```json
{
    "method": "configManager.getMemberNames",
    "params": {},
    "id": 999,
    "session": "<session_token>"
}
```

---

## Write Config

### Set EventHttpUpload

Configure HTTP event upload (AccessControl, DoorStatus) to the ADMS server.

```json
{
    "method": "configManager.setConfig",
    "params": {
        "name": "EventHttpUpload",
        "table": {
            "Enable": true,
            "Type": "digest",
            "UploadServerList": [
                {
                    "Address": "<adms_server>",
                    "AuthEnable": false,
                    "EventType": ["AccessControl", "DoorStatus"],
                    "HttpsEnable": false,
                    "Password": "",
                    "Port": 60087,
                    "Uploadpath": "/",
                    "UserName": ""
                }
            ]
        }
    },
    "id": 1000,
    "session": "<session_token>"
}
```

### Set AutoUpload

Configure auto event upload to the ADMS server.

```json
{
    "method": "configManager.setConfig",
    "params": {
        "name": "AutoUpload",
        "table": {
            "Enable": true,
            "Type": "digest",
            "UploadServerList": [
                {
                    "Address": "<adms_server>",
                    "AuthEnable": false,
                    "EventType": ["AccessControl", "DoorStatus"],
                    "HttpsEnable": false,
                    "Password": "",
                    "Port": 60087,
                    "Uploadpath": "/",
                    "UserName": ""
                }
            ]
        }
    },
    "id": 1000,
    "session": "<session_token>"
}
```

### Set VSP_CGI

Configure device auto-registration to the ADMS server.

```json
{
    "method": "configManager.setConfig",
    "params": {
        "name": "VSP_CGI",
        "table": {
            "AutoRegister": {
                "DeviceID": "<device_serial>",
                "Enable": true,
                "Servers": [
                    {
                        "Address": "",
                        "Domain": "<adms_server>",
                        "HttpsEnable": false,
                        "Port": 60087,
                        "Type": 0
                    }
                ]
            },
            "ServiceStart": true
        }
    },
    "id": 1000,
    "session": "<session_token>"
}
```

### Set Timezone (NTP)

Set timezone to Jakarta and configure NTP server.

```json
{
    "method": "configManager.setConfig",
    "params": {
        "name": "NTP",
        "table": {
            "Address": "time.windows.com",
            "Enable": false,
            "Port": 123,
            "TimeZone": 12,
            "TimeZoneDesc": "Jakarta",
            "UpdatePeriod": 10
        }
    },
    "id": 1000,
    "session": "<session_token>"
}
```

### Set _DHCloudUpgradeRecord_

Configure cloud upgrade check settings.

```json
{
    "method": "configManager.setConfig",
    "params": {
        "name": "_DHCloudUpgradeRecord_",
        "table": {
            "AutoCheck": 1,
            "CheckInterval": 1380,
            "LastSubVersion": "",
            "LastVersion": "Eng_PN_V3.002.0000002.0.R.20250307",
            "ProxyAddr": "updatev2.easy4ipcloud.com",
            "ProxyPort": 443,
            "Upgrade": 0,
            "downloadState": 1,
            "packageId": ""
        }
    },
    "id": 1000,
    "session": "<session_token>"
}
```

---

## User Management

### Change Password

Uses CGI endpoint with Digest Auth.

```
GET http://<device-ip>/cgi-bin/userManager.cgi?action=modifyPassword&name=admin&pwd=<new_password>&pwdOld=<old_password>
```

With curl:
```bash
curl --digest -u admin:<old_password> \
  "http://<device-ip>/cgi-bin/userManager.cgi?action=modifyPassword&name=admin&pwd=<new_password>&pwdOld=<old_password>"
```
