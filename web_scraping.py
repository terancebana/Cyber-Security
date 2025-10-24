import requests

URL = 'https://postman-echo.com/headers'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'Custom-Header': 'this-is-my-custom-header'
}

response = requests.get(url=URL, headers=headers).json()
print(response['headers']['user-agent'])
print(response['headers']['custom-header'])