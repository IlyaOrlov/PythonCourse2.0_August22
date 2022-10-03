class Duck:
    color = "Brown"

    def __init__(self, name, weight: int):
        self.name = name
        self.weight = weight

    @staticmethod
    def crack():
        print("Crack")

    @classmethod
    def duck_color(cls):
        print(f"Duck color is {cls.color}")

    def duck_parameters(self):
        print(f"Duck name is {self.name}. {self.name} weight is {self.weight}")

    def __repr__(self):
        return f"{self.name} said: Dont call me man, I'm eating"

    def __lt__(self, other):
        return self.name if self.weight > other.weight else other.name

    def __ne__(self, other):
        return self.weight is other.weight

    def __add__(self, other):
        return self.weight + other.weight


duck_one = Duck("Bob", 3)
duck_two = Duck("Rob", 3)
duck_one.crack()
duck_one.duck_color()
duck_one.duck_parameters()
print(duck_one)
print(f"The biggest duck is {duck_one > duck_two}")
print(f"Is {duck_one.name}'s weight equal {duck_two.name}'s weight? {duck_one != duck_two}")
print(f"You have {duck_one + duck_two} kg of DUCK MEAT")
