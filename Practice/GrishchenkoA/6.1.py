class MyTanks:
    "Класс содержит виды танков c характеристиками"
    color = "green"


    def __init__(self, damage, rate_of_fire, ammunition, speed, strength):
        self.damage = damage
        self.rate_of_fire = rate_of_fire
        self.ammunition = ammunition
        self.speed = speed
        self.strength = strength

    @staticmethod
    def print_res(lst):
        for i in lst:
            print(i.__dict__)


su_76i = MyTanks(156, 16, 170, 50, 285)
su_85i = MyTanks(280, 14, 70, 50, 500)
k_91_pt = MyTanks(530, 7, 30, 52, 1600)
print(MyTanks.__doc__)
lst_tanks = [su_76i, su_85i, k_91_pt]
MyTanks.print_res(lst_tanks)


