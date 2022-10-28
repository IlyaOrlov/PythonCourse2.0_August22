import multiprocessing.pool as mp_pool
import kafka
import kafka.errors as kafka_errors


class LimitedMultiprocessingPool(mp_pool.Pool):
    def get_pool_cache_size(self):
        return len(self._cache)


class MsgConsumer:
    def __init__(self, proc_fun):
        # Функция для обработки сообщения в дочернем процессе
        self.proc_fun = proc_fun
        # Клиент для чтения сообщений из Kafka
        self.consumer = kafka.KafkaConsumer(
            "example_topic",
            enable_auto_commit=False,
            bootstrap_servers=["127.0.0.1:9092"],
            group_id="example",
            client_id="example-backend",
        )
        # Лимит на количество сообщений, единовременно находящихся в пуле
        self.pool_cache_limit = 20
        # Флаг управляемой остановки приложения
        self.stop_processing = False
        # Пул обработчиков сообщений
        self.pool = LimitedMultiprocessingPool(processes=10)

    def handle_pool_cache_excess(self):
        while self.pool.get_pool_cache_size() >= self.pool_cache_limit:
            # Здесь можно предусмотреть sleep
            pass

    def main_loop(self):
        while not self.stop_processing:
            for msg in self.consumer:
                if self.stop_processing:
                    break
                try:
                    self.handle_pool_cache_excess()
                    self.consumer.commit()
                except kafka_errors.CommitFailedError:
                    # Отлавливаем редкий, но возможный случай исключения при ребалансе
                    continue
                self.pool.apply_async(self.proc_fun, (msg,))


def fun(*args, **kwargs):
    print(f"Received from Kafka: {args}")
    for arg in args:
        print(f"Received value: {getattr(arg, 'value').decode()}")


if __name__ == "__main__":
    consumer = MsgConsumer(fun)
    consumer.main_loop()
