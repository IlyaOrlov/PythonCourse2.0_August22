# -*- coding: utf-8 -*-
import socket
import pickle


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.35'
port = 64698
s.bind((host, port))
s.listen(2)
conn, addr = s.accept()
print('Server got connection from {}'.format(addr))
while True:
    data = conn.recv(1024)
    if not data:
        break
    data1 = pickle.loads(data)
    d = {"house": "дом", "car": "машина", "three": "дерево", "cat": "кошка", "apple": "яблоко"}
    c = d.keys()
    a = []
    for i in c:
        for y in data1:
            if y == i:
                a.append(d[i])
    conn.send(pickle.dumps(a))
conn.close()
