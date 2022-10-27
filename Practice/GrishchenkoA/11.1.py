# -*- coding: utf-8 -*-

import time
import threading
import multiprocessing

def find_primes(*args):
    if len(args) == 1:
        start = 3
        end = args[0]
    else:
        start = args[0]
        end = args[1]

    lst = []
    for i in range(start, end + 1):
        if i > 1:
            for y in range(2, i):
                if i % y == 0:
                    break
            else:
                lst.append(i)
    return lst

if __name__ == "__main__":
    lst_time = []
    start = time.perf_counter()
    find_primes(10000)
    find_primes(10001, 20000)
    find_primes(20001, 30000)

    lst_time.append(time.perf_counter() - start)
    print(f"Общее время обычного расчета занял в секундах: {lst_time}")

    start = time.perf_counter()  # считаем что-то много раз с разными параметрами
    lst_time1 = []
    thr1 = threading.Thread(target=find_primes, args=(10000,))
    thr2 = threading.Thread(target=find_primes, args=(10001, 20000))
    thr3 = threading.Thread(target=find_primes, args=(20001, 30000))
    thr1.start() #  если 'забыть' выполнить start, то будет ошибка RuntimeError: cannot join thread before it is started
    thr2.start()
    thr3.start()
    thr1.join() #  если 'забыть' выполнить join, то ошибки не будет, но выполнится только один поток
    thr2.join()
    thr3.join()
    lst_time1.append(time.perf_counter() - start)
    print(f"Общее время расчета через многопоточность занял в секундах: {lst_time1}")

    start = time.perf_counter()
    lst_time2 = []
    p1 = multiprocessing.Process(target=find_primes, args=(10000,))
    p2 = multiprocessing.Process(target=find_primes, args=(10001, 20000))
    p3 = multiprocessing.Process(target=find_primes, args=(20001, 30000))
    p1.start() #  если 'забыть' выполнить start, то будет ошибка AssertionError: can only join a started process
    p2.start()
    p3.start()
    p1.join() #  если 'забыть' выполнить join, то ошибки не будет, но выполнится только один процесс
    p2.join()
    p3.join()
    lst_time2.append(time.perf_counter() - start)
    print(f"Общее время расчета через многопроцессорность занял в секундах: {lst_time2}")

# Быстрее всего данная задача решается через многопоточность