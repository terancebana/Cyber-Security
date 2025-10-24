import requests
from bs4 import BeautifulSoup

URL = 'http://example.com'

response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup.title.text)
links = soup.find_all('a')

for link in links:
    print(link.get('href'))