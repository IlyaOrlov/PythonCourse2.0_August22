# Спроектировать класс Duck, при создании экземпляров которого будут задаваться атрибуты
# name, weight, а атрибут color должен быть общим для всех экземпляров класса.
# Также в классе должны быть методы:

class Duck:
    color = 'grey'
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @staticmethod # - статический метод, выводящий «Сrack»;
    def crack():
        return 'Сrack'

    @classmethod # - классовый метод, выводящий цвет уток;
    def col(cls):
        cls.color = Duck.color
        return f'Цвет уток {Duck.color}'

    def __repr__(self): # - методы экземпляров: метод, выводящий имя и вес утки; метод __repl__ ;
        return f'Утка {self.name} весит {self.weight}'

    def __lt__(self, other): # метод,принимающий 2х уток, и возвращающий имя более тяжелой утки (__lt__) ;
        if self.weight > other.weight:
            return f'утка {self.name} с большим весом в {self.weight} кг'
        else:
            return f'утка {other.name} с большим весом в {other.weight} кг'

    def __ne__(self, other): #метод, сравнивающий вес 2х уток и возвращающий bool (равен вес или нет (__ne__)) ;
        if self.weight == other.weight:
            return True
        else:
            return False

    def __add__(self, other):#метод, суммирующий вес 2х уток(__add__).
        return self.weight + other.weight

duck1 = Duck('Kiki', 5)
duck2 = Duck('Biggi', 5)
duck3 = Duck('Mikki', 4)
duck4 = Duck('Nikki', 3)
lst = [duck1, duck2, duck3, duck4]
print(lst)
print(duck4.col())
print(duck3.crack())
print(duck1 > duck2)
print(duck1 == duck2)
print(duck1 + duck2)























