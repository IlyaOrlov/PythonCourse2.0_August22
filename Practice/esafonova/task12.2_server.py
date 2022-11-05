#Написать клиентское и серверное приложения.
# Клиент при установке соединения отправляет на сервер информацию о пользователе (имя, возраст),
# хранимую в атрибутах объекта класса User.
# Сервер должен выводить информацию о подключенных пользователях.
# Клиентское приложение должно быть запущено несколько раз с различными пользователями.
import socket
import pickle
import threading


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Пользователь {} возраст {} лет'.format(self.name, self.age)

class ClientTh(threading.Thread):

    def __init__(self, conn, addr):
        super().__init__()
        self._conn = conn
        self._addr = addr

    def run(self):
        print(f'Сервер соеденился с клиентом {self._addr}. '
              f'{pickle.loads(self._conn.recv(1024))}')


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None
        self._run = False

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self.host, self.port))
        self._socket.listen(5)
        self._run = True

        while self._run:
            conn, addr = self._socket.accept()
            ClientTh(conn, addr).start()

    def stop(self):
        self._runn = False
        self._socket.close()


if __name__ == "__main__":
    ser = Server('127.0.0.1', 888)
    try:
        ser.run()
    except KeyboardInterrupt:
        ser.stop()





