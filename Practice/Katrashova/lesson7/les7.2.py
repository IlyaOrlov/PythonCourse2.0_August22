import time
import random

class Man:

    def __init__(self, name):
        self.name = name
    def solve_task(self):
        print("I'm not ready yet")

class Pupil(Man):
    def solve_task(self):
        delay = random.randint(3, 6)
        time.sleep(delay)
        super().solve_task()


man = Man("Альберт")
pupil = Pupil("Арнольд")
man.solve_task()
pupil.solve_task()