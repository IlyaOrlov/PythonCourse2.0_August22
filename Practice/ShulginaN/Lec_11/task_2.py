# Реализовать запуск функции, осуществляющей операцию сложения для различных типов (integer, string, list)
# параллельно с различными наборами аргументов.

import multiprocessing


def my_sum(*args):
    if isinstance(args[0], int):
        print(sum(args))
        return sum(args)
    elif isinstance(args[0], str):
        my_str = ''
        for i in range(len(args)):
            my_str += args[i]
        print(str(my_str))
        return my_str
    elif isinstance(args[0], list):
        lst = []
        for i in range(len(args)):
            lst += args[i]
        print(lst)
        return lst


if __name__ == "__main__":

    processes = [multiprocessing.Process(target=my_sum, args=(['139', 'hh', 'pp'])),
                 multiprocessing.Process(target=my_sum, args=(130, 12, 98)),
                 multiprocessing.Process(target=my_sum, args=('Hello', ' ', 'world', '!'))]
    for process in processes:
        process.start()
    for process in processes:
        process.join()

