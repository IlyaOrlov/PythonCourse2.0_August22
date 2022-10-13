import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.connect((host, port)) # подключаемся к серверу
d = s.recv(1024) # получаем данные от сервера (1024 байта - размер буфера для данных)
while d:
    print(d.decode())
    d = s.recv(1024)
# преобразуем данные из байтового представления в строковое и выводим
# (преобразование из utf-8 в ascii)
s.close()
