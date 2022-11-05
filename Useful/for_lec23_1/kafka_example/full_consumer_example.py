import multiprocessing as mp
import multiprocessing.pool as mp_pool
import signal
import time
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
            "labeling",
            auto_offset_reset="earliest",
            enable_auto_commit=False,
            bootstrap_servers=["127.0.0.1:9092"],
            group_id="labeling",
            client_id="labeling-backend",
            check_crcs="false",
            consumer_timeout_ms=1000,
            session_timeout_ms=30000,
            request_timeout_ms=30500,
            max_partition_fetch_bytes=2000000000
        )
        # Лимит на количество сообщений, единовременно находящихся в пуле
        self.pool_cache_limit = 20
        self.graceful_shutdown_timeout = 600
        # Флаг управляемой остановки приложения
        self.stop_processing = False
        # Пул обработчиков сообщений
        self.pool = LimitedMultiprocessingPool(processes=10)
        # Обеспечиваем возможность остановки приложения по SIGTERM
        signal.signal(signal.SIGTERM, self.set_stop_processing)

    def set_stop_processing(self, *args, **kwargs):
        self.stop_processing = True

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

    def graceful_shutdown(self):
        try:
            self.consumer.close()  # Останавливаем клиента Kafka
            self.pool.close()  # Предотвращаем добавление новых задач в пул
            graceful_shutdown_end = time.time() + self.graceful_shutdown_timeout
            while graceful_shutdown_end > time.time():
                active_child_proc_num = len(mp.active_children())
                if active_child_proc_num == 0:
                    break
                # Здесь можно предусмотреть sleep
            else:
                raise
        except Exception as ex:
            self.pool.terminate()
            raise ex
        finally:
            self.pool.join()


def fun(*args, **kwargs):
    print("Do nothing")


if __name__ == "__main__":
    consumer = MsgConsumer(fun)
    consumer.main_loop()
    consumer.graceful_shutdown()
