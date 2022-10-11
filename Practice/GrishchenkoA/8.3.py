import time

class Manager_Time:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = time.time() - self.start
        print(f"Время выполнения программы заняло: {self.stop} секунд")


with Manager_Time():
    for i in range(100000):
        i += i