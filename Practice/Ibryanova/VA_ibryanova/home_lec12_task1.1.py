import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 147
cip = {
    'q': 'й',
    'w': 'ц',
    'e': 'у',
    'r': 'к',
    't': 'е',
    'y': 'н',
}

server.bind((host, port))
server.listen(5)

while True:
    conn, addr = server.accept()
    s = conn.recv(2024).decode()
    print(f'Получено "{"".join(s)}" от клиента {addr}.')

    res = []
    key = {v: k for k, v in cip.items()}
    for i in s:
        try:
            res.append(key[i])
        except KeyError:
            print('ошибка')


    conn.send((''.join(res)).encode())
    print('Успешно')
    conn.close()
server.close()