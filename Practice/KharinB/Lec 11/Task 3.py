import threading as th

# Создать несколько потоков таким образом, чтоб каждый из них мог хранить приватные данные, доступные только ему самому.
# Запустить потоки с одной функцией, выводящей в каждом потоке его имя и приватные данные
# (имя исполняемого потока можно узнать, используя current_thread().name из библиотеки threading).

def thread_info(num):
    print(f"Номер потока {num}") # Номер подойдёт для персональных данных?
    print(th.current_thread().name)
    input()
    print(num**2) # Выводит квадрат номера потока
    print(th.current_thread().name)
    input()


def run_thread(quantity):
    if quantity < 1:
        raise TypeError
    threads = []
    for i in range(1, quantity+1):
        thread = th.Thread(target=thread_info, args=(i,))
        thread.start()
        threads.append(thread)

    for j in threads:
        j.join()
        print("Потоки закрыты")


run_thread(3)
