# Создать несколько потоков таким образом, чтоб каждый из них мог хранить приватные данные,
# доступные только ему самому. Запустить потоки с одной функцией, выводящей в каждом потоке его имя и приватные данные
# (имя исполняемого потока можно узнать, используя current_thread().name из библиотеки threading).
import threading


class MyPrivateThread(threading.Thread):
    def __init__(self, x):
        threading.Thread.__init__(self)
        self._x = x

    def run(self):
        print(f'Имя потока: {threading.current_thread().name}, данные: {self._x}')


threads = [
    MyPrivateThread('Тут мой логин'),
    MyPrivateThread('Тут мой пароль')
]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
