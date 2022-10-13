import time
from math import sqrt
from threading import Thread
from multiprocessing import Process


def find_primes(*args):
    if len(args) == 2:
        start = args[0]
        end = args[1]
    else:
        start = 3
        end = args[0]
    for number in range(start, end):
        switcher = True
        i = 2
        while i <= sqrt(number):
            if number % i == 0:
                switcher = False
                break
            i += 1
        if switcher:
            return number


if __name__ == "__main__":
    time_list = []
    # обычный способ
    start = time.perf_counter()
    find_primes(10000)
    find_primes(10001, 20000)
    find_primes(20001, 30000)
    time_list.append(time.perf_counter() - start)
    # многопоточность
    start = time.perf_counter()
    thr1 = Thread(target=find_primes, args=(10000,))
    thr2 = Thread(target=find_primes, args=(10001, 20000))
    thr3 = Thread(target=find_primes, args=(20001, 30000))
    # Если не выполнить запуск потока, то экземпляр класса Thread не запустится -> не выполнится target
    thr1.start()
    thr2.start()
    thr3.start()
    # Если не выполнить join() для каждого потока, то самый быстрый поток, закончив работу, сообщит главному потоку,
    # что можно двигаться дальше к строке time_list....
    thr1.join()
    thr2.join()
    thr3.join()
    time_list.append(time.perf_counter() - start)
    # многопроцессность
    start = time.perf_counter()
    p1 = Process(target=find_primes, args=(10000,))
    p2 = Process(target=find_primes, args=(10001, 20000))
    p3 = Process(target=find_primes, args=(20001, 30000))
    # Если не выполнить запуск процесса, то экземпляр класса Process не запустится -> не выполнится target
    p1.start()
    p2.start()
    p3.start()
    # Если не выполнить join() для каждого процесса, то самый быстрый процесс, закончив работу,
    # сообщит главному процессу, что можно двигаться дальше к строке time_list....
    p1.join()
    p2.join()
    p3.join()
    time_list.append(time.perf_counter() - start)
    for i in time_list:
        print(f'{i:.10f} sec.')
    # Так как функция по нахождению простых чисел внутри себя имеет просто вычисление,
    # без каких-либо вводов, остановок - она будет иметь лучшее время из всех представленных способов.
    # Многопоточность показала себя хуже, потому что как только из созданных потоков приостановился,
    # тут сразу же влез другой поток, то есть они друг друга тормозят. Получается некий хаос.

    # Не знаю по какой причине многопроцессность показала себя хуже остальных. Скорее всего это связано
    # с return, но осознания пока что не пришло.
