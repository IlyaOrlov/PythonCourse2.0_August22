# Два потока запрашивают и выводят координаты точки на плоскости
from threading import Thread, RLock
import time


class Base:
    x = 0
    y = 0


lock = False

def print_fun(r):
    i = 0
    global lock
    while i < 2:
        # while lock is True:
        #     time.sleep(1)
        # lock = True
        with r:
            Base.x = input("2x: ")
            Base.y = input("2y: ")
            print(f'Thread 2: Base.x = {Base.x}, Base.y = {Base.y}')
        i += 1
        time.sleep(1)


if __name__ == '__main__':
    r = RLock()
    t = Thread(target=print_fun, args=(r,))
    t.start()
    i = 0
    while i < 2:
        # while lock is True:
        #     time.sleep(1)
        # lock = True
        with r:
            Base.x = input("1x: ")
            Base.y = input("1y: ")
            print(f'Thread 1: Base.x = {Base.x}, Base.y = {Base.y}')
        i += 1
        time.sleep(1)
    t.join()
