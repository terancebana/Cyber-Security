import socket

HOST = 'example.com'
PORT = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

http_request = f'GET / HTTP/1.1\r\nHost: {HOST}\r\nConnection: close\r\n\r\n'
client.send(http_request.encode())

response_data = client.recv(4096)

print(response_data.decode())
client.close()