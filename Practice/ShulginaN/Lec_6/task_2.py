#  Спроектировать класс Duck, при создании экземпляров которого будут задаваться атрибуты name, weight,
#  а атрибут color должен быть общим для всех экземпляров класса. Также в классе должны быть методы:
# - статический метод, выводящий «Сrack»;
# - классовый метод, выводящий цвет уток;
# - методы экземпляров: метод, выводящий имя и вес утки; метод __repr__ ;
#  метод, принимающий 2х уток, и возвращающий имя более тяжелой утки (__lt__) ;
#  метод, сравнивающий вес 2х уток и возвращающий bool (равен вес или нет (__ne__)) ;
#  метод, суммирующий вес 2х уток(__add__).

class Duck:

    color = "yellow"

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @staticmethod
    def crack_met():
        print("Сrack")

    @classmethod
    def color_met(cls):
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


duck1 = Duck("Donald", 50)
duck2 = Duck("Martin", 60)

duck1.crack_met()
duck2.color_met()
print(duck1)
print(duck2)
print(duck1 < duck2)
print(duck1 != duck2)
print(f"Общий вес уток {duck1 + duck2} кг")
