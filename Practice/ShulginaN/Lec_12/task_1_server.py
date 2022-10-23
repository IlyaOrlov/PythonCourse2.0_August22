import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 123
cipher = {
    'а': 'a',
    'б': 'b',
    'в': 'с',
    'г': 'd',
    'д': 'e',
    'е': 'f',

}

server.bind((host, port))
server.listen(10)

while True:
    conn, addr = server.accept()
    s = conn.recv(1024).decode()
    print(f'Получено "{"".join(s)}" от клиента {addr}.')

    res = []
    no_key = {v: k for k, v in cipher.items()}
    for i in s:
        try:
            res.append(no_key[i])
        except KeyError:
            print("Ошибка")


    conn.send((''.join(res)).encode())
    print("Успешно")
    conn.close()
server.close()

