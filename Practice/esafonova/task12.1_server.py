import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 555
cipher = {
    'П': 'a',
    'р': 'b',
    'и': 'c',
    'в': '.',
    'е': ',',
    'т': 'd',
    ' ': 'i',
    'д': 'f',
    'у': 'w',
    'г': 'e'
}

server.bind((host, port))
server.listen(10)

while True:
    conn, addr = server.accept()
    s = conn.recv(1024).decode()
    print(f'Получено "{"".join(s)}" от клиента {addr}.')

    res = []
    decipher = {v: k for k, v in cipher.items()}
    for i in s:
        try:
            res.append(decipher[i])
        except KeyError:
            print('Ошибка')


    conn.send((''.join(res)).encode())
    print("Успешно дешифровано")
    conn.close()
server.close()