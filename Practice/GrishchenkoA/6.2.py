class Duck:
    color = "grey"
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


    @staticmethod
    def say_Duck():
        print("Crack")


    @classmethod
    def color_duck(cls):
        print(f"Цвет уток: {Duck.color}")


    def __repr__(self):
        return f"Имя утки: {self.name}, вес утки: {self.weight} грамм"


    def __lt__(self, other):
        return {other.name}


    def __ne__(self, other):
        return self.weight != other.weight


    def __add__(self, other):
        return self + other




d1 = Duck("Billy", 700)
d2 = Duck("Willy", 900)
d3 = Duck("Dilly", 800)
d1.say_Duck()
Duck.color_duck()
print(repr(d1))
print(repr(d2))
print(repr(d3))
print(d2 < d3)
print(d1 != d2)
print(d1.weight.__add__(d3.weight))
