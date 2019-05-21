import socket

HOST = "127.0.0.1"
PORT = 65432

#AF_INET = IPv4
#SOCK_STREAM = TCP

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello World")
    data = s.recv(4096)

print("Received", repr(data))