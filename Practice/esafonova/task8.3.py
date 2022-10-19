#Напишите свой менеджер контекста, замеряющий и показывающий время исполнения кода внутри него.
import time


class MyManagerContext:
    def __enter__(self):
        self._start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(time.time() - self._start)


with MyManagerContext():
    a = ''
    for i in range(0, 10000000):
        if i % 9 == 0:
            a += str(i) + ','

