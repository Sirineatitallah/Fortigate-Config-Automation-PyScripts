import requests
import json

url = "https://192.168.52.133/api/v1/AdminLogin/"

payload = json.dumps({
  "name": "restapi",
  "password": "sirine"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YWRtaW5hcGk6c2lyaW5l',
  'Cookie': 'APSCOOKIE_ffbe3e4d0e3350075e9c91f574e799cc_RESTFUL=Era%3D0%26Payload%3DEgWYa3TQYvaFDz75n9JHNQDga0uB653MS5P0yUdVNUMAlrN5lZA85vFD345H1ch9%0A%2Fs3WC4qZ8y8HJB71f4giK774ieOLoQHc3FvQ7wiDEwu%2FfWexsIYdiBUY0q3hBmmw%0AwxrDP3t1WWdbYUdtv02rRRt42mo403wca2p4yzq37MXQ%2BGOq6WjHI1a1x%2FCQLnTV%0A38ta3TGPNq28R%2FEZAUT2Hg%3D%3D%0A%26AuthHash%3DVdkr%2BfSD%2BM2SEl3XCPqHznvtKZ0%3D%0A%26'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
