import pickle
import socket


def server_program():
    host = socket.gethostname()  # получаем имя ПК на котором запускается сервер
    port = 5080  # выбираем порт на котором будем работать
    server_socket = socket.socket()  # создаем сокет
    server_socket.bind((host, port))  # подключаемся на выбранный нами порт для ожидания подключений от клиентов
    server_socket.listen(2)  # выбираем максимальное количество клиентов.
    conn, address = server_socket.accept()  # ждем подключение клиента
    print("Connection from: " + str(address))  # выводим соощение, что клиент подключился
    # создаем словарь для расшифровки
    shifr_dict = {'dasd': 'hello', 'rewff': 'my', 'gvavasdf': 'dear', 'fdasferv': 'friend'}
    while True:
        # получаем данные от клиента
        data = conn.recv(1024)
        if not data:
            break
        # преобразуем получинные данные от клиента в список зашифрованных слов
        shifrs = pickle.loads(data)
        message = []
        # проводим расшифровку слов согласно слованя
        for shifr in shifrs:
            # формируем массив расшифрованных слов.
            message += [shifr_dict[shifr]]
        # отправляем расшифрованный список назад клиенту.
        conn.send(pickle.dumps(message))
    conn.close()


# запускаем сервер
if __name__ == '__main__':
    server_program()
