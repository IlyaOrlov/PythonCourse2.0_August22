import time
import random

class Man:
    def __init__(self, name):
        self._name = name
        
    def solve_task(self):
        print("I'm not ready yet")
        
myman = Man("Иван")

print(myman._name)
myman.solve_task()

# 2.Написать класс Pupil,у которого переопределен метод solve_task.
# На этот раз он будет думать от 3 до 6 секунд (c помощью метода sleep библиотеки time и randint библиотеки random).

class Pupil(Man):
    def __init__(self, pupilname):
        self._pupilname = pupilname
        
    def solve_task(self):
        time.sleep(random.randint(3, 6))
        print("I'm not ready yet")
        
        
mypupil = Pupil("Сергей")
print(mypupil._pupilname)
# for people in (myman, mypupil):
mypupil.solve_task()