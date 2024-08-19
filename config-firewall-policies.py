#ALLOW LAN TO WAN
import requests
import json

url = "http://192.168.52.137/api/v2/cmdb/firewall/policy?access_token=qsyfr6zHt0bqt9m7N8sf97rt0mH4jg"

payload = json.dumps({
  "json": {
    "name": "LAN_to_WAN",
    "policyid": 100,
    "srcintf": [
      {
        "name": "port1"
      }
    ],
    "dstintf": [
      {
        "name": "port2"
      }
    ],
    "srcaddr": [
      {
        "name": "all"
      }
    ],
    "dstaddr": [
      {
        "name": "all"
      }
    ],
    "action": "accept",
    "schedule": "always",
    "service": [
      {
        "name": "ALL"
      }
    ],
    "logtraffic": "all",
    "nat": "enable"
  }
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

#ALLOW VIP
import requests
import json

url = "http://192.168.52.137/api/v2/cmdb/firewall/policy?access_token=qsyfr6zHt0bqt9m7N8sf97rt0mH4jg"

payload = json.dumps({
  "json": {
    "name": "vip",
    "srcintf": [
      {
        "name": "port2"
      }
    ],
    "dstintf": [
      {
        "name": "port1"
      }
    ],
    "srcaddr": [
      {
        "name": "all"
      }
    ],
    "dstaddr": [
      {
        "name": "Access my ip users"
      }
    ],
    "schedule": "always",
    "service": [
      {
        "name": "ALL"
      }
    ],
    "action": "accept",
    "nat": "enable",
    "ippool": "disable",
    "logtraffic": "all",
    "comments": "Write a comment…",
    "inspection-mode": "proxy",
    "ssl-ssh-profile": "no-inspection",
    "status": "enable"
  }
})
headers = {
  'Content-Type': 'application/json',
  'access_token': '••••••'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
