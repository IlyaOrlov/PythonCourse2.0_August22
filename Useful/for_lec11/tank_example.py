import random


class Tank:
    MODEL = "Tank"

    def __init__(self, power, armour):
        self._power = power
        self._armour = armour

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, new_power):
        if type(new_power) is int:
            self._power = new_power

    def show(self):
        print(f"{self.MODEL} {self._power}, {self._armour}")


class T34(Tank):
    MODEL = "T34"

    def shoot(self):
        print("Bah")


class Tiger(Tank):
    MODEL = "Tiger"

    def shoot(self):
        print("Ba-bah")


class Abrams(Tank):
    MODEL = "Abrams"

    def shoot(self):
        print("Ba-ba-bah")


lst = [T34(30, 30), Tiger(80, 80), Abrams(90, 90)]
while True:
    i = input("Next step (stop to stop): ")
    if i == "stop":
        break

    t = random.choice(lst)
    t.power = input("Input power ")
    t.power += 1
    t.shoot()
    t.show()

