# Спроектировать класс Duck, при создании экземпляров которого будут задаваться атрибуты
# name, weight, а атрибут color должен быть общим для всех экземпляров класса.
# Также в классе должны быть методы:

class Duck:
    _color = 'grey'
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    @staticmethod # - статический метод, выводящий «Сrack»;
    def crack():
        return 'Сrack'

    @classmethod # - классовый метод, выводящий цвет уток;
    def col(cls):
        return f'Цвет уток {cls._color}'

    def __repr__(self): # метод __repl__ ;
        return f'Утка {self._name} весит {self._weight}'

    def __str__(self):
        return f'Утка {self._name} весит {self._weight}'# - методы экземпляров: метод, выводящий имя и вес утки;

    def __lt__(self, other): # метод,принимающий 2х уток, и возвращающий имя более тяжелой утки (__lt__) ;
        if self._weight > other._weight:
            return f'утка {self._name} с большим весом в {self._weight} кг'
        else:
            return f'утка {other._name} с большим весом в {other._weight} кг'

    def __ne__(self, other): #метод, сравнивающий вес 2х уток и возвращающий bool (равен вес или нет (__ne__)) ;
        if self._weight != other._weight:
            return False
        else:
            return True

    def __add__(self, other):#метод, суммирующий вес 2х уток(__add__).
        return self._weight + other._weight

duck1 = Duck('Kiki', 5)
duck2 = Duck('Biggi', 5)
duck3 = Duck('Mikki', 4)
duck4 = Duck('Nikki', 3)
lst = [duck1, duck2, duck3, duck4]
print(lst)
print(duck4.col())
print(duck3.crack())
print(duck1 > duck2)
print(duck1 != duck2)
print(duck1 + duck2)























