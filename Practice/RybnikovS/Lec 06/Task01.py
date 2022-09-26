import random


class Tank:

    def __init__(self):
        all_fractions = ("Allies", "Soviet")
        all_weights = ("Light", "Medium", "Heavy")
        self.fraction = all_fractions[int(input("Press: 0 - Play as Allies, 1 - Play as Soviet: "))]
        self.weight = all_weights[int(input("Press: 0 - Play on Light, 1 - Play on Medium, 2 - Play on Heavy: "))]

    def __repr__(self):
        return f"You play on {self.weight} tank, with {self.health()} HP. You fight for {self.fraction}"

    def wrap_action(func):
        def inside(*args):
            print("===========")
            func(*args)

        return inside

    def health(self):
        dict_health = {"Light" : 300, "Medium" : 600, "Heavy" : 1000}
        inc_health = {"Allies" : 1.2, "Soviet" : 0.9}
        health = dict_health[self.weight] * inc_health[self.fraction]
        return health

    def damage_per_shot(self):
        basic_damage = 75
        dict_speed_damage = {"Light" : 1.3, "Medium" : 1, "Heavy" : 0.8}
        inc_damage = {"Allies" : 0.8, "Soviet" : 1.15}
        shot = basic_damage * dict_speed_damage[self.weight] * random.randint(1, 100) / 100 * inc_damage[self.fraction]
        return shot

    @wrap_action
    def move_or_die(self):
        your_choice = int(input("Move Or Die! For <moving> press 0, for <shot> press 1, for <surrender> press 9: "))
        if your_choice == 0 :
            print("Your position has been changed")
        if your_choice == 1 :
            print(f"Boom! You dealt {self.damage_per_shot()} damage. Your HP is {self.current_health}")
        if your_choice == 9 :
            print(f"You lost the battle, but not the war")
            exit()

    def current_hp(self, inner_health, taken_damage):
        inner_health -= taken_damage
        return inner_health

    current_health = 0


my_tank = Tank()
print(my_tank)
my_tank.current_health = my_tank.health()
while True:
    my_tank.current_health = my_tank.current_hp(my_tank.current_health, random.randint(1, 50))
    my_tank.move_or_die()
