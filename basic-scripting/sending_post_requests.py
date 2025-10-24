import requests

URL = 'https://postman-echo.com/post'

payload = {
    'username' : 'test_user',
    'level' : 10
}

response = requests.post(url=URL, data=payload).json()
print(response['data'])