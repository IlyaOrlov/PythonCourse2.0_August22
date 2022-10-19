#Напишите свой менеджер контекста
import time

class Fragment:
    def __enter__(self):
        print('Старт')
        self.start = time.time()


    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Финиш')
        self.end = time.time() - self.start
        print(f'код выполнен за: {self.end} секунды')

lst = range(0, 100)

with Fragment():
    for i in lst:
        print(i)