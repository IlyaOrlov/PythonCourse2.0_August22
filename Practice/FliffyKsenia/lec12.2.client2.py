# клиент для подключения к серверу и при подключении говорит своё имя и возраст, и держит соединение открытым. пока пользователь не наберет Bye.
import socket
import pickle


class User():
    def __init__(self, name, age):
        self.name = name
        self.age = age
# функция которая принимает объект типа юзер и передает этот объект серверу.
def client_program(user):
    host = socket.gethostname()  # получаем имя компьютера на котором запускается клиент, считаем, что сервер запущен на этом же ПК.
    port = 5089  # порт к которому будем подключатся.
    client_socket = socket.socket()  # инициализируем сокет
    client_socket.connect((host, port))  # подключаемся к серверу
    text = ""
    while text.lower().strip() != 'bye':
        client_socket.send(pickle.dumps(user))  # запаковываем объект типа юзер и передаем его серверу.
        text = input("for exit, enter bye -> ")  # ждем ввода пользователя, для поддержания соединения
    client_socket.close()  # Закрываем соединеие

if __name__ == '__main__':
    # Создаем объект типа юзер именем и возрастом.
    user = User("Mary",24)
    client_program(user)
