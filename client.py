import socket
import uuid

# По порту 8000 передаем ID и получаем ещё один
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_id = uuid.uuid4().bytes
client_sock.connect(('127.0.0.1', 8000))
client_sock.sendall(bytes(client_id))
cid = client_sock.recv(1024)
client_sock.close()

# По порту 8001 передаем сообщение указанным способом
client_sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock1.connect(('127.0.0.2', 8001))
print('Введите сообщение, котрое будет передано на сервер:')
message = str(input())
client_sock1.sendall(bytes(cid))
client_sock1.sendall(bytes(client_id))
client_sock1.sendall(bytes(message, encoding='utf8'))
data = client_sock1.recv(1024)
client_sock1.close()
print(repr(data))
