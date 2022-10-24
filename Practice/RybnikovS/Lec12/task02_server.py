import socket
import pickle
from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int


host = '127.0.0.1'
port = 80
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))
server.listen(5)

while True:
    conn, addr = server.accept()
    s = conn.recv(1024)
    print(f'Установлена связь с {addr} пользователь {pickle.loads(s)}')
    conn.close()
server.close()