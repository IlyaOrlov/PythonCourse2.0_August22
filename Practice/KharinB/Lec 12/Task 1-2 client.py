import socket
import multiprocessing as mp # для запуска подключения различных пользователей
import random


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def connect_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 55345
    s.connect((host, port))
    return s


def decoder_in_serv(message): # Часть из задания 1
    s = connect_server()
    message = "decod" + message
    s.send(message.encode())
    d = s.recv(1024)
    s.close()
    return d.decode()


def user_export(us): # Часть из задания 2
    s = connect_server()
    s.send(f"Пользователь {us.name}, возраст {us.age}".encode())
    s.close()


def users_process(users):
    process = []
    for _ in range(int(users)):
        name = random.choice(("Иван", "Алексей", "Марина", "Матильда", "Леопольд"))
        age = random.randint(1, 100)
        us = User(name, age)
        proc = mp.Process(target=user_export, args=(us,))
        proc.start()
        process.append(proc)

    for proc in process:
        proc.join()


if __name__ == "__main__":
    print(decoder_in_serv("@%##+-*!$^-#$!)!№-;№!:^("))
    users_process(input("Ведите количество пользователей: "))

