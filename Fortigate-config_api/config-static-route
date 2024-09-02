import requests
import json

url = "http://192.168.52.137/api/v2/cmdb/router/static?access_token=qsyfr6zHt0bqt9m7N8sf97rt0mH4jg"

payload = json.dumps({
  "json": {
    "dst": "0.0.0.0 0.0.0.0",
    "gateway": "192.168.5.254",
    "device": "port2",
    "distance": 10,
    "comment": "Route par defaut"
  }
})
headers = {
  'Content-Type': 'application/json',
  'access_token': '••••••'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
