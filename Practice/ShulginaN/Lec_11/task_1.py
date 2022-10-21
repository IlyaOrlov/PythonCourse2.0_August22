# Написать функцию find_primes(end, start), которая ищет все простые числа в диапазоне от заданного числа start
# (по умолчанию 3) до заданного числа end. Далее необходимо:
# Запустить ее три раза последовательно в диапазоне от 3 до 10000, от 10001 до 20000, от 20001 до 30000.
# Запустить ее три раза с теми же аргументами, но каждый раз в отдельном потоке с помощью threading.Thread.
# Запустить ее три раза с теми же аргументами, но каждый раз в отдельном процессе с помощью multiprocessing.Process.
#
# Замерить время исполнения каждого варианта и сравнить результаты.
# В данном случае, через потоки и обычную функцию быстрее, чем через процессы. Потому, что для запуска процесса
# затрачивается больше времени(у процесса все свое - сегмент кода, сегмент данных, стек), чем для запуска потока
# (у потоков же разные только стек) и выполнение функции.


# Что будет, если 'забыть' выполнить start или join для процессов?
#    start - процессы не запустятся, выпадет исключение
#    join - основной процесс выполнится без ожидания остальных
# Что будет, если 'забыть' выполнить start или join для потоков?
#    start - потоки будут созданы, но не запустятся
#    join - главный поток выполнится не дождавшись отсальных


import multiprocessing
import threading
import time
import math


def find_primes(start, end):
    lst = []
    for i in range(start, end + 1):
        a = int(math.sqrt(end))
        for j in range(start, a + 1):
            if i % j == 0:
                break
            else:
                lst.append(i)
        print(len(lst))
        return lst


if __name__ == "__main__":
    start_time = time.time()
    find_primes(3, 10000)
    find_primes(10001, 20000)
    find_primes(20001, 30000)
    res = time.time() - start_time
    print(res)

    start_time = time.time()
    th1 = threading.Thread(target=find_primes, args=(3, 10000))
    th2 = threading.Thread(target=find_primes, args=(10001, 20000))
    th3 = threading.Thread(target=find_primes, args=(20001, 30000))
    th1.start()
    th2.start()
    th3.start()
    th1.join()
    th2.join()
    th3.join()
    res2 = time.time() - start_time
    print(res2)

    start_time = time.time()
    mp1 = multiprocessing.Process(target=find_primes, args=(3, 100000))
    mp2 = multiprocessing.Process(target=find_primes, args=(100001, 200000))
    mp3 = multiprocessing.Process(target=find_primes, args=(200001, 300000))
    mp1.start()
    mp2.start()
    mp3.start()
    mp1.join()
    mp2.join()
    mp3.join()
    res3 = time.time() - start_time
    print(res3)

