import socket
import sys

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <target_host>")
    sys.exit()

TARGET_URL = sys.argv[1]
PORTS = [21, 22, 80, 443, 8080]
    
for port in PORTS:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1.0)
    
    result = client.connect_ex((TARGET_URL, port))

    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")
    
    client.close()

print("Scanning complete...")