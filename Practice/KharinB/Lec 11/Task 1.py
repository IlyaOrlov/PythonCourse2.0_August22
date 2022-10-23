import math
import time
import threading
import multiprocessing

def find_primes(start, end):
    if start> end:
        end, start = start, end
    elif start == end:
        print("Неверный диапазон")
        return None
    else:
        res = []
        while start < end:
            start_iter = 2
            end_iter = math.sqrt(start)
            while start_iter <= end_iter:
                if start % start_iter == 0:
                    break
                else:
                    start_iter += 1
            else:
                res.append(start)
            start += 1
        return res


if __name__ == "__main__":
    start_t = time.time()
    find_primes(3, 100000)
    find_primes(100001, 200000)
    find_primes(200001, 300000)
    end1 = time.time()-start_t
    print(end1)
    # Увеличил числа в 10 раз, потому что иначе не показательно... процессы создаются дольше, чем функция выполняется

    start_t = time.time()
    th1 = threading.Thread(target=find_primes, args=(3, 100000))
    th2 = threading.Thread(target=find_primes, args=(100001, 200000))
    th3 = threading.Thread(target=find_primes, args=(200001, 300000))
    th1.start() # Без старта поток не запустится, основной поток дойдя до join не поймёт чего ждёт и выдаст исключение
    th2.start()
    th3.start()
    th1.join()
    th2.join()
    th3.join()
    end2 = time.time()-start_t
    print(end2)
    # Без join главный поток выполнится не дождавшись побочных потоков.


    start_t = time.time()
    mp1 = multiprocessing.Process(target=find_primes, args=(3, 100000))
    mp2 = multiprocessing.Process(target=find_primes, args=(100001, 200000))
    mp3 = multiprocessing.Process(target=find_primes, args=(200001, 300000))
    mp1.start() #Если процесс не запустить, то интерпритатор выдаст исключение. Ничего не запущено, нечего и ждать.
    mp2.start()
    mp3.start()
    mp1.join()
    mp2.join()
    mp3.join()
    end3 = time.time()-start_t
    print(end3)
    # Если не печатать join, то основной процесс выполнится без ожидания.
    # То есть время посчитается и выведится без учёта выполнения побочных процессов.