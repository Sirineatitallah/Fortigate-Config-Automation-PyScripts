https://192.168.52.140/api/v1/domain/domain1.local/PolicyIp/2
post 
import requests
import json

url = "https://192.168.52.140/api/v1/domain/domain1.local/PolicyIp/2"

payload = json.dumps({
  "mkey": 2,
  "client_type": 0,
  "client": "0.0.0.0/0",
  "client_geoip_group": "",
  "client_ip_group": "",
  "client_isdb": "",
  "server_type": 0,
  "server": "192.168.52.0/24",
  "server_ip_group": "",
  "status": True,
  "session_profile": "Outbound_Session@system",
  "antispam_profile": "",
  "antivirus_profile": "",
  "content_profile": "",
  "profile_dlp": "",
  "ip_pool_profile": "",
  "auth_type": 0,
  "radius_auth": "",
  "ldap_auth": "",
  "pop3_auth": "",
  "imap_auth": "",
  "smtp_auth": "",
  "exclusive": False,
  "comment": ""
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic cmVzdGFwaTpzaXJpbmU=',
  'Cookie': 'APSCOOKIE_ffbe3e4d0e3350075e9c91f574e799cc_RESTFUL=Era%3D0%26Payload%3DAVaBVUhfL6Q4dLMQ1qnKWd566sCqDgch7LMy0TpvpzX3MPaunEh6efkToSQbw%2BW9%0ATbyU8BPpm0ZoGPlAUzV5tdrbvRzP7xxlKVUJa4Ly%2FZT7X3h125CLVVObMx0hUKL5%0Aj5oDcxlkYBUVp%2B1y4yGx8fIn3gsu0t2R2R0Maa9y9VvR2D7UB%2FpC2lcbChdx6W86%0Akp4Dea1811yCcu305OWaLQ%3D%3D%0A%26AuthHash%3DyFRDhWg8y7s5CHoo1w7TLg0JSFk%3D%0A%26'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
