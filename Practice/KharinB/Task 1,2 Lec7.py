import random
import time

class Man:
    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print("I'm not ready yet")


class Pupil(Man):
    def solve_task(self):
        print("wait a bit")
        time.sleep(random.randint(3, 6))
        print("I'm not ready yet")


man_one = Man("Donny")
man_two = Pupil("Barbara")

print(f"{man_one.name=}")
man_one.solve_task()

print(f"{man_two.name=}")
man_two.solve_task()