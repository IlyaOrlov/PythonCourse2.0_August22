import threading
import random
import time


def secret_info(*args):
    print(f"Поток {threading.current_thread().name} имеет данные {random.randint(1, 20)}")
    time.sleep(random.randint(1, 2))
    print(f"Поток {threading.current_thread().name} закрыт")

th_quantity = 4
threads = []
for i in range(0, th_quantity):
    cur_thread = threading.Thread(target=secret_info, args=(i,))
    cur_thread.start()
    threads.append(cur_thread)

for th in threads:
    th.join()

