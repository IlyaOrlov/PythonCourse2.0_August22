import time
import random


class Pupil:
    def __init__(self, name):
        self._name = name

    def solve_task(self):
        print("I'm not ready yet")


class Tim(Pupil):
    def solve_task(self):
        n = random.randint(3, 6)
        time.sleep(n)
        super().solve_task()


res = Tim('Дмитрий')
res.solve_task()