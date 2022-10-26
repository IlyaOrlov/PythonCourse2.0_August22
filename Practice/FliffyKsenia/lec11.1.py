import time
from threading import Thread
import multiprocessing as mp

start_1 = 3
end_1 = 10000
start_2 = 10001
end_2 = 20000
start_3 = 20001
end_3 = 30000

class MyError(Exception):
    pass

class Mythread(Thread):
    def __init__(self,*args):  # переопределяем процедуру инициализации
        Thread.__init__(self)  # выполняем процедуру инициализации из родительского класса
        self.args = args
    def run(self):  # описываем функцию которая начинает работать при старте потока.
       self.lst = find_primes(*self.args)


def superfun(fun):
    def inner_fun(*args, **kwargs):
        start = time.time()
        res = fun(*args, **kwargs)
        stop = time.time()
        print(f"Execution time: {stop - start}")
        return res

    return inner_fun

def find_primes(*args):
    match len(args):
        case 1:
            start, end  = 3, args[0]
        case 2:
            start, end  = args[0],args[1]
        case _:
            raise MyError("too many arguments")

    if start <= 2 and end > 2:
        lst = [2]
        start = 3
    else:
        lst = []
    for i in range(start, end + 1, 2):

        if not ((i > 10) and (i % 10 == 5)):

            for j in range(3, i + 1, 2):
                if (i % j == 0):
                    break
                if j * j > i:
                    lst.append(i)
                    break


    return lst

@superfun
def pusk():
    return find_primes(end_1) + find_primes(start_2, end_2) + find_primes(start_3, end_3)


@superfun
def thread_pusk():
    mytread1 = Mythread(end_1)
    mytread2 = Mythread(start_2,end_2)
    mytread3 = Mythread(start_3,end_3)
    mytread1.start()
    mytread2.start()
    mytread3.start()
    mytread1.join()
    mytread2.join()
    mytread3.join()
    return mytread1.lst + mytread2.lst + mytread3.lst



def foo(*args):
    args[0].put(find_primes(args[1],args[2]))



@superfun
def process_pusk():
    mp.set_start_method('spawn')
    q1 = mp.Queue()
    q2 = mp.Queue()
    q3 = mp.Queue()
    p1 = mp.Process(target=foo, args=(q1,start_1,end_1))
    p2 = mp.Process(target=foo, args=(q2,start_2,end_2))
    p3 = mp.Process(target=foo, args=(q3,start_3,end_3))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    return q1.get() + q2.get() + q3.get()


if __name__ == '__main__':
    print("Запускаем последовательно процедуру")
    print(f"Найдено {len(pusk())} простых чисела")
    print("Запускаем процедуру через потоки")
    print(f"Найдено {len(thread_pusk())} простых чисела")
    print("Запускаем через процессы")
    print(f"Найдено {len(process_pusk())} простых чисела")