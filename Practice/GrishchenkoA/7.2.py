import random
import time


class Man:
    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print("I'm not ready yet")


class Pupil(Man):
    def solve_task(self):
        time_new = random.randint(3, 6)
        res = time.sleep(time_new)


Pupill_1 = Pupil("Svetlana")
Man_1 = Man("Petr")
Man_1.solve_task()
print(Pupill_1.name)

