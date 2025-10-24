import requests

url = "http://example.com"
response = requests.get(url)

if response.status_code == 200:
    print(response.status_code)
    print(response.headers['Content-Type'])
    print(response.content[:150])