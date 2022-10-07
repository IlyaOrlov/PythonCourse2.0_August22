# Написать класс Pupil, у которого переопределен метод solve_task. На этот раз он будет думать от 3 до 6 секунд
# (c помощью метода sleep библиотеки time и randint библиотеки random).

import time
import random


class Man:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def solve_task():
        print("I'm not ready yet")


class Pupil(Man):

    def solve_task(self):
        time.sleep(random.randint(3, 6))
        super().solve_task()


m = Man("Натали")
m.solve_task()

