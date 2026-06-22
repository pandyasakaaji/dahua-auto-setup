# Dahua Face Recognition Access Controller CGI

### Tested on

* **Model:** DHI-ASI3204E
* **System Version:** V3.002.0000002.0.R.20250307
* **Security Baseline Version:** V2.4

## Getting Configuration

### Get All Configuration Names

```json
{
  "method": "configManager.getMemberNames",
  "params": {},
  "id": 999,
  "session": ""
}
```

### Get a Specific Configuration

Once the configuration name has been identified, a specific configuration can be retrieved using the `configManager.getConfig` method by providing the `name` parameter.

```json
{
  "method": "configManager.getConfig",
  "params": {
    "name": "methodNames"
  },
  "id": 999,
  "session": ""
}
```

For example, to retrieve the `Auto Upload` configuration:

```json
{
  "method": "configManager.getConfig",
  "params": {
    "name": "EventHttpUpload"
  },
  "id": 999,
  "session": ""
}
```

Example response:

```json
{
  "id": 999,
  "params": {
    "table": {
      "Enable": true,
      "Type": "digest",
      "UploadServerList": [
        {
          "Address": "",
          "AuthEnable": false,
          "EventType": [
            "AccessControl",
            "DoorStatus"
          ],
          "HttpsEnable": false,
          "Password": "",
          "Port": 0,
          "Uploadpath": "/",
          "UserName": ""
        }
      ]
    }
  },
  "result": true,
  "session": ""
}
```

After retrieving the configuration, verify that the `table` field contains the settings you intend to modify. The retrieved `table` object can then be used as the basis for the update request.

## Updating Configuration

### Auto Upload

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
          "Address": "",
          "AuthEnable": false,
          "EventType": [
            "AccessControl",
            "DoorStatus"
          ],
          "HttpsEnable": false,
          "Password": "",
          "Port": 0,
          "Uploadpath": "/",
          "UserName": ""
        }
      ]
    }
  },
  "id": 1000,
  "session": ""
}
```

### DHCPIPv4

To toggle IPv4 DHCP option, use the following CGI:

```json
{
  "method":"configManager.setConfig",
  "params":{
    "name":"Network",
    "table":{
      "DefaultInterface":"eth0",
      "Domain":"dauha",
      "Hostname":"BSC",
      "eth0":{
        "DefaultGateway":"x.x.x.x",
        "DhcpEnable":true, // or false
        "DnsServers":[
          "",
          ""
        ],
        "EnableDhcpReservedIP":false,
        "IPAddress":"x.x.x.x",
        "MTU":1500,
        "PhysicalAddress":"xx:xx:xx:xx:xx:xx",
        "SubnetMask":"x.x.x.x"
      }
    }
  },
  "id":999,
  "session":""
}
```
