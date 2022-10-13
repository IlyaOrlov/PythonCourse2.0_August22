import time


class MyCtxManager:
    def __enter__(self):
        self.time = time.time()
        print("Начинаем отсчет времени на операцию")

    def __exit__(self, type, value, traceback):
        self.time = time.time() - self.time
        print(f"Обработка операции заняла: {self.time}")


with MyCtxManager():
    print("Wait a moment, please")
    time.sleep(5)

