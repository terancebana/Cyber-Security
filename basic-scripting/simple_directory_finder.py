import requests

URL = 'http://example.com'
wordlist = ['admin', 'login', 'robots.txt', 'test-page', '']

for page in wordlist:
    try:       
        full_url = f"{URL}/{page}"
        
        response = requests.get(full_url)
        if response.status_code == 200:
            print(f"[+] Found: {full_url}")
        elif response.status_code == 404:
            print(f"[-] Not Found: {full_url}")
        else:
            print(f"[?] Received code: {response.status_code} for {full_url}")
    
    except requests.exceptions.RequestException:
        print(f"[!] Connection error for: {full_url}")
        
    
 
