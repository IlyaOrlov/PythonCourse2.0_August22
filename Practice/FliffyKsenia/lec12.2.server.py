# сервер который ждет подключения от клиентов, и при каждом новом подключении выдает список активных клиентов с именами пользователей.
import socket
import pickle
from threading import Thread
from lec12_2_imports import User

PORT = 5089


# создаем класс для создания потока который будет обрабатывать входящие соединения
class Server_thread(Thread):
    def __init__(self, conn, addr):  # переопределяем процедуру инициализации
        Thread.__init__(self)  # выполняем процедуру инициализации из родительского класса
        self.conn, self.addr = conn, addr  # сохраняем в свойства данные о соединении
        self.notready = True  # создаем парамерт, который сообщает нам получили ли мы данные о пользователе или нет. True не получили, False  получили
        self.not_die = True

    def server_stop(self):
        self.conn.settimeout(1)
        self.conn.close()
        self.conn.detach()

    def run(self):  # описываем функцию которая начинает работать при старте потока.
        while True:
            data = self.conn.recv(1024)  # принимаем данные от клиента
            if not data:
                self.conn.close()  # если нет данных закрываем соединиение
                self.not_die = False
                break  # выходим из потока, завершая его.
            else:
                self.user = pickle.loads(
                    data)  # обрабатываем данные от клиента и создаем переменную внутри класса типа юзер.
                self.notready = False  # сообщаем классу, что мы получили данные о пользователе


class Server_main(Thread):
    def __init__(self, port):
        Thread.__init__(self)
        self.port = port  # задаем имя порта на котором будем ждать соединения
        self.threads = []  # объявляем массив для хранения текущих подключений

    def server_stop(self):
        self.server_start = False  # говорим серверу, что рабочий день закончен.
        for t in self.threads:  # обходим живые потоки
            t.server_stop()  # говорим им, что рабочий день закончен.
        client_socket = socket.socket()  # инициализируем сокет для того, чтобы закрыть сервер, надо выйти из состояния ожидания соединения. для этого фиктивно конектимся. по факту этим говори стоп.
        client_socket.connect((self.host, self.port))  # подключаемся к серверу
        user = User("", 0)  # создаем фикивного пользователя, чтбы не вызывать ошибку.
        client_socket.send(pickle.dumps(user))  # запаковываем объект типа юзер и передаем его серверу.
        client_socket.close()  # закрываем соединиение

    def run(self):
        self.server_start = True  # переменная состояния сервера.
        self.host = socket.gethostname()  # получаем имя текущего компа на котором запустился наш сервер
        self.server_socket = socket.socket()  # создаем сокет
        self.server_socket.bind((self.host, self.port))  # открываем заданный порт для прослушивания
        self.server_socket.listen(20)  # задаем количество возможных соединений
        while self.server_start:
            conn, addr = self.server_socket.accept()  # ждем подключения
            threada = Server_thread(conn, addr)  # создаем и запускаем новый поток для обработки данных от клиента
            threada.start()  # запускаем новый поток.
            self.threads.append(threada)  # добавляем наш поток в список активных потоков
        self.server_socket.close()  # закрываем соединение

    def connected_users(self):
        print("Connected users:")  # выводим список подключенных пользователей
        for thread in self.threads:  # обходим массив активных соединений.
            if thread.not_die:  # проверяем на живость потока, если умер, то удаляем из массыва живых потоков.
                while thread.notready:  # ждем когда прийдет информация о пользователе
                    pass
                print(f"name: {thread.user.name}, age: {thread.user.age}")  # выводим данные об активном соединении
            else:
                self.threads.remove(thread)  # удаляем умерший поток


is_runinng = ""
myserver = Server_main(PORT)  # создаем поток сервера.
myserver.start()  # запускаем сервер в отдельном потоке.

while is_runinng != "bye":
    is_runinng = input(
        "Введите bye для выхода, или любой текст для просмотра подключенных клиентов:")  # ждем команды пользователя
    myserver.connected_users()  # выводим текущие соединения.

myserver.server_stop()  # останавливаем сервер.
print("Bye!")
