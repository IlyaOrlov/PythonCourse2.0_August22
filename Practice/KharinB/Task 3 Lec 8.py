import time
class MyManager:
    def __enter__(self):
        self._start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(time.time() - self._start)

with MyManager():
    print("Text")

with MyManager():
    time.sleep(5)