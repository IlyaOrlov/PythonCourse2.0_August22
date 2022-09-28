import random


class Tank:

    def __init__(self, my_fraction, my_weight):
        all_fractions = ("Allies", "Soviet")
        all_weights = ("Light", "Medium", "Heavy")
        self.fraction = all_fractions[my_fraction]
        self.weight = all_weights[my_weight]

    def __repr__(self):
        return f"You play on {self.weight} tank, with {self.health} HP. You fight for {self.fraction}"

    @staticmethod
    def wrap_action(func):
        def inside(*args):
            print("===========")
            func(*args)

        return inside

    def max_health(self):
        self.health = self.dict_health[self.weight] * self.inc_health[self.fraction]

    def damage_per_shot(self):
        shot = self.basic_damage * self.dict_speed_damage[self.weight] * random.randint(1, 100) \
               / 100 * self.inc_damage[self.fraction]
        return round(shot)

    @wrap_action
    def move_or_die(self):
        your_choice = int(input("Move Or Die! For <moving> press 0, for <shot> press 1, for <surrender> press 9: "))
        if your_choice == 0:
            print("Your position has been changed")
        if your_choice == 1:
            print(f"Boom! You dealt {self.damage_per_shot()} damage. Your HP is {self.health}")
        if your_choice == 9:
            print(f"You lost the battle, but not the war")
            exit()

    def current_hp(self, taken_damage):
        self.health -= taken_damage

    dict_health = {"Light": 300, "Medium": 600, "Heavy": 1000}
    inc_health = {"Allies": 1.2, "Soviet": 0.9}
    basic_damage = 75
    dict_speed_damage = {"Light" : 1.3, "Medium": 1, "Heavy": 0.8}
    inc_damage = {"Allies": 0.8, "Soviet": 1.15}
    health = 0
    current_health = 0


fraction = int(input("Press: 0 - Play as Allies, 1 - Play as Soviet: "))
weight = int(input("Press: 0 - Play on Light, 1 - Play on Medium, 2 - Play on Heavy: "))
my_tank = Tank(fraction, weight)
my_tank.max_health()
print(my_tank)
while True:
    my_tank.move_or_die()
    my_tank.current_hp(random.randint(1, 50))
