import socket
import os

# Открываем на прослушивание два нужных порта
log = 'logfile.txt'
serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('', 8000))
serv_sock.listen(50)

serv_sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock1.bind(('', 8001))
serv_sock1.listen(50)

checklist = []
cid = 1

while True:
    # При прихождении данных на нужный порт соответственно их обрабатываем
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    serv_sock.bind(('', 8000))
    serv_sock.listen(10)
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr, ' on port 8000')

    if client_addr != '':
        while True:
            # Пока клиент не отключился, читаем передаваемые
            # им данные и отправляем обратно cid
            data = client_sock.recv(1024)
            if not data:
                # Клиент отключился
                break
            client_sock.sendall(bytes(cid))
            checklist.append(data)
        client_sock.close()
        client_addr = ''
        cid += 1

    client_sock1, client_addr1 = serv_sock1.accept()
    print('Connected by', client_addr1, ' on port 8001')
    if client_addr1 != '':
        received = []
        while True:
            # Пока клиент не отключился, читаем передаваемые
            # им данные и отправляем результат их обработки обратно
            data = client_sock1.recv(1024)
            if not data:
                # Клиент отключился
                break
            received.append(data)
            if len(received) == 3:
                if checklist[0] == received[1]:
                    client_sock1.sendall(b'Your message was received')
                    if os.path.exists(str(log)):
                        txt = open(str(log), "a")
                    else:
                        txt = open(str(log), "w+")
                    txt.write('\nПринято от клиента с ID ' + str(received[1]) +
                              ':\n' + str(received[2]))
                    txt.close()
                else:
                    client_sock1.sendall(b'Data is illegal due to wrong ID')
        print('Closing connection')
        client_sock1.close()
        client_addr1 = ''
