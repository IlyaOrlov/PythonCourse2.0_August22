#Написать класс Pupil, у которого переопределен метод solve_task.
# На этот раз он будет думать от 3 до 6 секунд (c помощью метода sleep библиотеки time и randint библиотеки random).
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
        print("I'm not ready yet")

a = Man('Вася')
b = Pupil('Петя')
a.solve_task()
b.solve_task()