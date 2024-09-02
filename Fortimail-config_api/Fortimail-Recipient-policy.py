import requests
import json

url = "https://192.168.52.140/api/v1/domain/domain1.local/PolicyRcpt/2"

payload = json.dumps({
  "mdomain": "domain1.local",
  "mkey": 9,
  "status": True,
  "direction": 2,
  "sender_type": 0,
  "sender_pattern": "*",
  "sender_domain": "domain1.local",
  "sender_ldap_profile": "",
  "sender_email_address_group": "",
  "sender_pattern_regex": ".*",
  "profile_user_import_sender": "",
  "sender_import_attribute_name": "",
  "sender_import_attribute_value": "",
  "groupmode": 0,
  "recipient_pattern": "*",
  "recipient_domain": "*",
  "ldap_profile": "",
  "recipient_email_address_group": "",
  "recipient_pattern_regex": ".*",
  "profile_user_import_recipient": "",
  "recipient_import_attribute_name": "",
  "recipient_import_attribute_value": "",
  "antispam": "",
  "content": "",
  "profile_dlp": "",
  "antivirus": "",
  "misc": "",
  "auth": 0,
  "radius_auth": "",
  "ldap_auth": "",
  "pop3_auth": "",
  "imap_auth": "",
  "smtp_auth": "",
  "pkiauth": False,
  "pkiuser": "",
  "comment": ""
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic cmVzdGFwaTpzaXJpbmU=',
  'Cookie': 'APSCOOKIE_ffbe3e4d0e3350075e9c91f574e799cc_RESTFUL=Era%3D0%26Payload%3DzMfeV1bV8dcLTAnDtDEUEU%2FGLoIbJrPOgfxGBt%2F4MfHgzpiEK4iySJoNnfDkOxsV%0Ax8txEd%2BU0pJJpB11oRAATJI2kTUnznA8X1KPCUf2cUFTJdEsyd%2FKGaIEB7dRbf0w%0AUGhhZWPtqs%2BDEJaF9%2B0ajlXsRBcWkNEejqY5UAOvh2bKkC3t1b6W2tLtg6gXDX3C%0ADUFLGam9i21qNcdY9VMd7g%3D%3D%0A%26AuthHash%3D0sPiv%2F86y%2B%2BqxDzmdyPyRsxbDvE%3D%0A%26'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
