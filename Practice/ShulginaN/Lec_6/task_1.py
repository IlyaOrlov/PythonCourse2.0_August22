
import random


class Tank:
    m = "Танк"

    def __init__(self, armor, hit):
        self.armor = armor  #броня
        self.hit = hit #удар

    def show(self):
        print(f"{self.m},{self.armor}, {self.hit}")


class IS7(Tank):
    m = "ИС-7"

    def forward(self):
        print("Выехал ИС-7 ")


class KB5(Tank):
    m = "КВ-5"

    def forward(self):
        print("Выехал КВ-5 ")


class SU152(Tank):
    m = "СУ-152"

    def forward(self):
        print("Накрыла арта ")


lst = [IS7(100, 90), KB5(90, 80), SU152(30, 90)]

while True:
    i = input("Next step (stop to stop): ")
    if i == "stop":
        break

    t = random.choice(lst)
    t.show()
    t.forward()
    t.hit += 5
    t.show()
