#port1
import requests
import json

url = "http://192.168.52.137/api/v2/cmdb/system/interface/port1?access_token=qsyfr6zHt0bqt9m7N8sf97rt0mH4jg"

payload = json.dumps({
  "ip": "192.168.52.137 255.255.255.0",
  "allowaccess": "ping https ssh snmp http telnet fgfm radius-acct probe-response fabric ftm speed-test",
  "role": "lan",
  "vdom": "root",
  "alias": "LAN_Interface",
  "status": "up"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)



#port2
import requests
import json

url = "http://192.168.52.137/api/v2/cmdb/system/interface/port2?access_token=qsyfr6zHt0bqt9m7N8sf97rt0mH4jg"

payload = json.dumps({
  "ip": "192.168.5.12 255.255.255.0",
  "allowaccess": "ping https ssh snmp http telnet fgfm radius-acct probe-response fabric ftm speed-test",
  "role": "lan",
  "vdom": "root",
  "alias": "WAN_Interface",
  "status": "up"
})
headers = {
  'Content-Type': 'application/json',
  'access_token': 'qsyfr6zHt0bqt9m7N8sf97rt0mH4jg'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
