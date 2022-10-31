class Duck:
    color = "белый"

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @staticmethod
    def crack():
        print("Сrack")

    @classmethod
    def color_duck(cls):
        print(f"Цвет утки {cls.color}")

    def __repr__(self):
        return f"Имя утки: {self.name}, вес {self.weight} кг"

    def __lt__(self, other):
        if self.weight < other.weight:
            return f"Утка {other.name} тяжелее"
        else:
            return f"Утка {self.name} тяжелее"

    def __ne__(self, other):
        return self.weight != other.weight

    def __add__(self, other):
        return self.weight + other.weight


duck1 = Duck("Катя", 4)
duck2 = Duck("Вика", 5)

duck1.crack()
duck2.color_duck()
print(duck1)
print(duck2)
print(duck1 < duck2)
print(duck1 != duck2)
print(f"Общий вес уток {duck1 + duck2} кг")
