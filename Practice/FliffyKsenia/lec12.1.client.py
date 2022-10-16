import socket
import pickle

def client_program(shifr):
    host = socket.gethostname() # получаем имя компьютера на котором запускается клиент, считаем, что сервер запущен на этом же ПК.
    port = 5080 # порт к которому будем подключатся.
    client_socket = socket.socket() # инициализируем сокет
    client_socket.connect((host, port)) # подключаемся к серверу
    client_socket.send(pickle.dumps(shifr)) # отправляем сериаоизованный список
    data = client_socket.recv(1024) # ждем расшифрованные данные от сервера
    print(f'Deciphered words: {pickle.loads(data)}') # выводим расшифрованный список на экран
    client_socket.close() # Закрываем соединение

if __name__ == '__main__':
    # создаем список зашифрованных слов.
    shifr = ['dasd','rewff','gvavasdf','fdasferv']
    # вызываем клиент для подключения к серверу.
    client_program(shifr)
