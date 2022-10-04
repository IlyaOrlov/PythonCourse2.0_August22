import time
import random


class Man:
    def __init__(self, name):
        self.name = "name"

    @staticmethod
    def solve_task():
        print("I'm not ready yet")


class Pupil:
    def __init__(self):
        print("Новый класс")

    @staticmethod
    def solve_task():
        time.sleep(random.randint(3, 6))
        print("I'm not ready yet")
