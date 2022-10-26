# сервер который ждет подключения от клиентов, и при каждом новом подключении выдает список активных клиентов с именами пользователей.
import socket
import pickle
from threading import Thread
from lec12_2_imports import User


# создаем класс для создания потока который будет обрабатывать входящие соединения
class Server_thread(Thread):
    def __init__(self, conn, addr):                                         # переопределяем процедуру инициализации
        Thread.__init__(self)                                               # выполняем процедуру инициализации из родительского класса
        self.conn, self.addr = conn, addr                                   # сохраняем в свойства данные о соединении
        self.notready = True                                                # создаем парамерт, который сообщает нам получили ли мы данные о пользователе или нет. True не получили, False  получили

    def run(self):                                                          # описываем функцию которая начинает работать при старте потока.
        while True:
            data = self.conn.recv(1024)                                     # принимаем данные от клиента
            if not data:
                self.conn.close()                                           # если нет данных закрываем соединиение
                break                                                       # выходим из потока, завершая его.
            else:
                self.user = pickle.loads(data)                              # обрабатываем данные от клиента и создаем переменную внутри класса типа юзер.
                self.notready = False                                       # сообщаем классу, что мы получили данные о пользователе


def server_program():
    threads = []                                                            # объявляем массыв для хранения живых соединений
    host = socket.gethostname()                                             #  получаем имя текущего компа на котором запустился наш сервер
    port = 5089                                                             # задаем имя порта на котором будем ждать соединения
    server_socket = socket.socket()                                         # создаем сокет
    server_socket.bind((host, port))                                        # открываем заданный порт для прослушивания
    server_socket.listen(20)                                                # задаем количество возможных соединений
    while True:
        conn, addr = server_socket.accept()                                 # ждем подключения
        threada = Server_thread(conn, addr)                                 # создаем и запускаем новый поток для обработки данных от клиента
        threada.start()                                                     # запускаем новый поток.
        threads.append(threada)                                             # добавляем наш поток в список активных потоков
        print("Connected users:")                                           # выводим список подключенных пользователей
        for thread in threads:                                              # обходим массив активных соединений.
            if thread.is_alive:                                             # проверяем на живость потока, если умер, то удаляем из массыва живых потоков.
                while thread.notready:                                      # ждем когда прийдет информация о пользователе
                    pass
                print(f"name: {thread.user.name}, age: {thread.user.age}")  # выводим данные об активном соединении
            else:
                threads.remove(thread)                                      # удаляем умерший поток


server_program()  # запускаем сервер
