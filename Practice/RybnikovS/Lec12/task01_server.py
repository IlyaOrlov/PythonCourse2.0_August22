import socket


host = '127.0.0.1'
port = 80
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

crypt_key = {'К': 'q',
             'о': 'a',
             'н': 'z',
             'а': 's',
             'к': 'x',
             'т': 'e',
             ' ': 'd',
             'O': 'c',
             'K': 'r'}

server.bind((host, port))
server.listen(1)

while True:
    conn, addr = server.accept()
    s = conn.recv(1024).decode()
    print(f'Получено сообщение "{s}" от клиента {addr}.')
    message = ""
    decrypting_key = {value: key for key, value in crypt_key.items()}
    for i in s:
        try:
            message += decrypting_key[i]
        except KeyError:
            print('Ошибка')
    if message:
        print("Сообщение расшифровано и отправлено")
        conn.send((''.join(message)).encode())
    conn.close()
server.close()