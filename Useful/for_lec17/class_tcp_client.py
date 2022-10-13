import socket
import random
import time


class TcpClient:
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self._socket = None

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        time.sleep(3)
        self._socket.send(self.name.encode())
        data = self._socket.recv(1024)
        print(f'Received: {data.decode()}')
        self._socket.close()


if __name__ == '__main__':
    name = 'Python client ' + str(random.randint(1, 1000))
    myclient = TcpClient(host='127.0.0.1', port=5555, name=name)
    myclient.run()