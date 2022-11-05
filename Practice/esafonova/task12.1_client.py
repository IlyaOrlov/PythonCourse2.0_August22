#Написать клиентское и серверное приложения.
# Клиент отправляет на сервер список зашифрованных слов, сервер дешифрует слова по словарю
# и возвращает клиенту список расшифрованных слов. Клиент должен вывести полученный список.
import socket


host = '127.0.0.1'
port = 555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
client.send('abc.,difbwe'.encode())
print(f'Получено: "{client.recv(1024).decode()}"')

client.close()


