import time

class MyCtxManager:

    def __enter__(self):
        print('Начало')
        self.start_time = time.time()
        print(f'Счетчик времени запущен от начала эпохи "1 января 1970 года, 00:00:00 (UTC)": {self.start_time}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Конец')
        self.end_time = time.time() - self.start_time
        print(f'На обработку команды затрачено: {self.end_time}')



lst = range(1, 50000)

with MyCtxManager():
    for i in lst:
        print(i)

