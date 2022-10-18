#Реализовать запуск функции, осуществляющей операцию сложения для различных типов (integer, string, list)
# параллельно с различными наборами аргументов.
import multiprocessing


def sum_mix(*args):
    if isinstance(args[0], int):
        print(sum(args))
        return sum(args)
    elif isinstance(args[0], str):
        st = ''
        for i in range(len(args)):
            st += args[i]
        print(str(st))
        return st
    elif isinstance(args[0], list):
        lst = []
        for i in range(len(args)):
            lst += args[i]
        print(lst)
        return lst

if __name__ == "__main__":

    processes = [multiprocessing.Process(target=sum_mix, args=(['12', 'a', '95'])),
                 multiprocessing.Process(target=sum_mix, args=(15, 18, 2)),
                 multiprocessing.Process(target=sum_mix, args=('Привет', ' ', 'мой', ' ', 'друг'))]
    for process in processes:
        process.start()
    for process in processes:
        process.join()


