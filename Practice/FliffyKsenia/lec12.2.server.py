# сервер который ждет подключения от клиентов, и при каждом новом подключении выдает список активных клиентов с именами.
import socket
import pickle
import time
from threading import Thread
# объявляем массыв для хранения живых соединений
threads = []
# объявляем класс юзер
class User():
    def __init__(self,name,age):
        self.name = name
        self.age = age
# создаем класс для создания потока который будет обрабатывать входящие соединения
class server_thread(Thread):
    def __init__(self, conn, addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr

    def run(self):
        while True:
            # принимаем данные от клиента
            data = self.conn.recv(1024)
            if not data:
                self.conn.close()
                # если соединение закрыто удаляем наш поток из списка активных соединений.
                threads.remove(self)
                break
            else:
                # обрабатываем данные от клиента и создаем переменную внутри класса типа юзер.
                self.user = pickle.loads(data)

def server_program():
    # получаем имя текущего компа на котором запустился наш сервер
    host = socket.gethostname()
    # задаем имя порта на котором будем ждать соединения
    port = 5089
    # создаем сокет
    server_socket = socket.socket()
    # открываем заданный порт для прослушивания
    server_socket.bind((host, port))
    # задаем количество возможных соединений
    server_socket.listen(20)
    while True:
        # ждем подключения
        conn, addr = server_socket.accept()
        # создаем и запускаем новый поток для обработки данных от клиента
        threada = server_thread(conn,addr)
        threada.start()
        # добавляем наш поток в список активных потоков
        threads.append(threada)
        # делаем паузу в работе программы, чтобы перед выводом списка подключенных пользователей клиент успел передать свое имя.
        time.sleep(1)
        # выводим список подключенных пользователей
        print("Connected users:")
        for thread in threads:
            # проверяем на живость потока, если умер, то удаляем из массыва живых потоков.
            if thread.is_alive:
                print(f"name: {thread.user.name}, age: {thread.user.age}")
            else:
                threads.remove(thread)

# запускаем сервер
if __name__ == '__main__':
    server_program()
