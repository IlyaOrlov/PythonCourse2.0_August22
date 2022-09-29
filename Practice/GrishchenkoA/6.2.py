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
        print(f"Имя утки: {self.name}, вес утки: {self.weight} грамм")


    def __lt__(self, other):
        return {other.name}


    def __ne__(self, other):
        return self


    def __add__(self, other):
        return self + other




d1 = Duck("Billy", 700)
d2 = Duck("Willy", 900)
d3 = Duck("Dilly", 800)
d1.say_Duck()
Duck.color_duck()
d1.__repr__()
d2.__repr__()
d3.__repr__()
print(d1.__lt__(d2))
print(d1.weight.__ne__(d2.weight))
print(d1.weight.__add__(d3.weight))
