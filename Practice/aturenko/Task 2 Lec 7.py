# 2. Спроектировать класс Duck, при создании экземпляров которого будут задаваться атрибуты name, weight, а атрибут color должен быть общим для всех экземпляров класса. Также в классе должны быть методы:
# - статический метод, выводящий «Сrack»;
# - классовый метод, выводящий цвет уток;
# - методы экземпляров: метод, выводящий имя и вес утки; метод __repl__ ;
# метод, принимающий 2х уток, и возвращающий имя более тяжелой утки (__lt__) ;
# метод, сравнивающий вес 2х уток и возвращающий bool (равен вес или нет (__ne__)) ;
# метод, суммирующий вес 2х уток(__add__).

class Duck:
    _color = "yellow"
    
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight
        
        
    @staticmethod    
    def outputCrack():
        print("Crack!")
        
    @classmethod
    def outputColor(cls):
        print(f"Цвет уток {cls._color}")
        
    
    def outputInfo(self):
        print(f"Имя утки {self._name}, вес {self._weight}")
        
        
    def __repr__(self):
        return f'Утка {self._name}, весит {self._weight}'
        
    def __lt__(self, other):
        if self._weight > other._weight:
            return f'Более тяжёлая утка - {self._name}'
            
    def __ne__(self, other):
        if self._weight != other._weight:
            return True
        else:
            return False
            
    def __add__(self, other):
        return self._weight + other._weight
        
duck1 = Duck("Donald", 4)
duck2 = Duck("Utka", 5)

duck1.outputCrack()
duck2.outputCrack()
duck1.outputColor()
duck1.outputInfo()
duck2.outputInfo()
print(duck1 > duck2)
print(duck1 == duck2)
print(duck1 + duck2)