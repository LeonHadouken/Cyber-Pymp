import requests

url = "http://local.adspower.net:50325/api/v1/browser/start?api-key=4cf15918ce42b1b7b12ca1f05e201f42&user_id=j5jx24k"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
