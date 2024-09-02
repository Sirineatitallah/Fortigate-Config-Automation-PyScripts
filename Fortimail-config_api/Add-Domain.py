import requests
import json

url = "https://192.168.52.133/api/v1/Domain/domain2.local"

payload = json.dumps({
  "mkey": "domain2.local",
  "ip": "192.168.52.137",
  "port": 25,
  "is_subdomain": False,
  "maindomain": "domain2.local",
  "mxflag": 0,
  "is_association": False,
  "is_service_domain": False,
  "recipient_verification": "SMTP",
  "ec_status": True,
  "failed_time": 1
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic cmVzdGFwaTpzaXJpbmU=',
  'Cookie': 'APSCOOKIE_ffbe3e4d0e3350075e9c91f574e799cc_RESTFUL=Era%3D0%26Payload%3DEgWYa3TQYvaFDz75n9JHNbblE7RWYm3KskkWYP2Hrm5%2BEx7vIkPWQhGRUsGv15nK%0A1Vn1hvHu5Dyqoa2GhCelJ%2FD4t9k34OWEQbEqCDRNYYlCeuZ9uwES6lSr1GAzwTt5%0Ayil1rgmfWXdNvx9uzTq7mbjogG6XSHWmCOre5eX0Zs77GhEe%2FESAdlU1FhtsZyh8%0AdURt2i7szxOtlyZ9oS013Q%3D%3D%0A%26AuthHash%3Df10fHDq3LMxESqwXVzgVH80qmRE%3D%0A%26'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


#dns 

http://192.168.52.133/api/v1/SysDns/
get
{
    "objectID": "SysDns:",
    "reqAction": 1,
    "nodePermission": 3,
    "primary": "192.168.5.130",
    "secondary": "8.8.8.8",
    "ptr_query_option": 0,
    "cache": true,
    "named": false,
    "truncate_handling": 1,
    "protected_domain_dns_state": false,
    "protected_domain_dns_servers": "",
    "cache_min_ttl": 300
}
