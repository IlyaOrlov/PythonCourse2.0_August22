import socket
import pickle
import random
import time
from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int


name_of_user = ["Petr", "Anton", "Alexandr"]

host = '127.0.0.1'
port = 80

while True:
    time.sleep(1.5)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    user = User(random.choice(name_of_user), random.randint(1, 99))
    client.send(pickle.dumps(user))
    client.close()

