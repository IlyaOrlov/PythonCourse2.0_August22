import socket

# 1-й параметр - семейство адресов, с которыми будет работать сокет
# AF_INET соответствует адресам IPv4
# 2-й параметр - протокол транспортного уровня
# SOCK_STREAM соотвествует протоколу TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'  # '127.0.0.1' соответствует хосту, на котором запускается скрипт
port = 12345
s.bind((host, port))
s.listen(5)  # Открываем порт на сервере (не более 5 клиентов одновременно)
while True:
    conn, addr = s.accept()
    print('Server got connection from {}'.format(addr))
    # Преобразуем строку в набор байтов (ascii в utf-8) и отправляем
    conn.send('Thank you for the connection'.encode())
    conn.close()
s.close()
