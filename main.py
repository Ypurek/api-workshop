import requests

url = "http://shopen.qamania.org/api/v1/pens?minLength=10"

payload = {}
headers = {
  'accept': 'application/json',
  'Authorization': 'e175e29c-da9f-44be-9a4e-b95278f251e4'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
