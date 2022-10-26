import time
import random


class Man:
    def solve_task(self):
        print("I'm not ready yet")


class Pupil(Man):
    def __init__(self,  begin_time = 3, end_time = 6):
        vremy_random = random.randint(begin_time, end_time)
        time.sleep(vremy_random)
        self.begin_time = begin_time
        self.end_time = end_time
        self.vremy_random = vremy_random


my_object = Pupil()
my_object.solve_task()