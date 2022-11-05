import time


class MyManagerContext:
    def __enter__(self):
        self._time_start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(time.time() - self._time_start)


with MyManagerContext():
    for i in range(1, 10000):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if len(output) == 0:
            output = str(i)
