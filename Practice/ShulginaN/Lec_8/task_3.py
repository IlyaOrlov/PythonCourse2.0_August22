# Напишите свой менеджер контекста, замеряющий и показывающий время исполнения кода внутри него.

import time


class MyCtxManager:
    def __enter__(self):
        print("Входим в менеджер контекста")
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Выходим из менеджера контекста")
        self.end = time.time() - self.start
        print(f"Время исполнения кода: {self.end}")


lst = range(1, 1000)

with MyCtxManager():
    for i in lst:
        print(i)




