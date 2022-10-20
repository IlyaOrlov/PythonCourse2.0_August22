import socket
import pickle


class User:                                      #  Cоздаем класс User
    def __init__(self, name, age):               #  объявляем процедуру инициализации
        self.name = name                         #  объявляем свойство Name
        self.age = age                           #  объявляем свойство Age


# клиент для подключения к серверу и при подключении говорит своё имя и возраст, и держит соединение открытым. пока пользователь не наберет Bye.
def client_program(user):
    host = socket.gethostname()                  # получаем имя компьютера на котором запускается клиент, считаем, что сервер запущен на этом же ПК.
    port = 5089                                  # порт к которому будем подключатся.
    client_socket = socket.socket()              # инициализируем сокет
    client_socket.connect((host, port))          # подключаемся к серверу
    text = ""
    client_socket.send(pickle.dumps(user))       # запаковываем объект типа юзер и передаем его серверу.
    while text.lower().strip() != 'bye':         # пока не получили стоп слово общаемся с сервером и удерживаем соединение.
        text = input("for exit, enter bye -> ")  # ждем ввода пользователя, для поддержания соединения
    client_socket.close()                        # Закрываем соединеие
