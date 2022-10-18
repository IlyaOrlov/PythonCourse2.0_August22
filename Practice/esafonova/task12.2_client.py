import socket
import pickle
import random
import time


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Пользователь {} возраст {} лет'.format(self.name, self.age)


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None

    def run(self):
        names = ['Игорь', 'Петр', 'Антон', 'Иван', 'Алексей']

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        time.sleep(5)
        self._socket.send(pickle.dumps(User(random.choice(names), random.randint(20, 36))))
        self._socket.close()


if __name__ == "__main__":
    my_client = Client(host = '127.0.0.1', port=888)
    my_client.run()