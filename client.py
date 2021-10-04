import socket
import uuid

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('127.0.0.1', 8000))
iden = uuid.uuid4()
client_sock.send(bytes(iden))
code = repr(client_sock.recv(1024))
client_sock.close()
print('Received', code)