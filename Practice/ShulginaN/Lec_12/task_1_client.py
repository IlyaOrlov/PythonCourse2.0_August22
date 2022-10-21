# Написать клиентское и серверное приложения. Клиент отправляет на сервер список зашифрованных слов, сервер
# # дешифрует слова по словарю и возвращает клиенту список расшифрованных слов. Клиент должен вывести полученный список.


import socket


host = '127.0.0.1'
port = 123

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
client.send('abcdef'.encode())
print(f"Получено сообщение: {client.recv(1024).decode()}")

client.close()
