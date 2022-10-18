#Написать функцию find_primes(start, end), которая ищет все простые числа в диапазоне от заданного числа start
# (по умолчанию 3) до заданного числа end. Далее необходимо:
#Запустить ее три раза последовательно в диапазоне от 3 до 10000, от 10001 до 20000, от 20001 до 30000.
#Запустить ее три раза с теми же аргументами, но каждый раз в отдельном потоке с помощью threading.Thread.

# Что будет, если 'забыть' выполнить start или join для потоков?
# Ответ: Start - потоки создадутся, но не будут запущены. Выпадет исключение.
#        Join - потоки создадутся, запустятся, но выполнятся позже первого процесса

#Запустить ее три раза с теми же аргументами, но каждый раз в отдельном процессе с помощью multiprocessing.Process.


# Что будет, если 'забыть' выполнить start или join для процессов?
# Ответ: Start - процессы создадутся, но не будут запущены. Выпадет исключение.
#        Join - процессы создадутся, запустятся, но выполнятся позже главного процесса

#Замерить время исполнения каждого варианта и сравнить результаты.
# Ответ: через процессы быстрее.
import multiprocessing
import threading
import time


def find_primes(start, end):
    lst = []
    for i in range(start, end + 1):
        for j in range(2, i):
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
    work_time = time.time() - start_time
    print(work_time)

    start_time = time.time()
    threads = [threading.Thread(target=find_primes, args=(3, 10000)),
               threading.Thread(target=find_primes, args=(10001, 20000)),
               threading.Thread(target=find_primes, args=(20001, 30000))]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    work_time = time.time() - start_time
    print(work_time)

    start_time = time.time()
    processes = [multiprocessing.Process(target=find_primes, args=(3, 10000)),
                 multiprocessing.Process(target=find_primes, args=(10001, 20000)),
                 multiprocessing.Process(target=find_primes, args=(20001, 30000))]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    work_time = time.time() - start_time
    print(work_time)
