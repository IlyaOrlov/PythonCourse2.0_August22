import time
import random

class Man:
    def __init__(self, name):
        self.name = name

    # @staticmethod
    def solve_task(self):
        print("I'm not ready yet")


class Pupil(Man):
    # @staticmethod
    def solve_task(self):
        time.sleep(random.randint(3, 6))
        super().solve_task()


human = Pupil("Steve")
human.solve_task()
