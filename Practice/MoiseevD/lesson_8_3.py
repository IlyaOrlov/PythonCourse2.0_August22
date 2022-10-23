import time


class timeManager:

    def __enter__(self):
        self.t1 = time.time()
        print(f'Запуск таймера в менеджере контекста {self.t1}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.t2 = time.time() - self.t1
        print('Остановка таймера менеджера контекста')
        print(f'Время исполнения кода {self.t2}')


lst =range(2, 100000)
with timeManager():
    for i in lst:
        print(i)
