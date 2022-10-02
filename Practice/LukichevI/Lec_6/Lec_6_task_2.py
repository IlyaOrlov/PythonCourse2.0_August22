class Duck:
    color = ('Серый')

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @staticmethod
    def crack():
     print('Кря кря!')

    @classmethod
    def duck_color(cls):
        print(f'Цвет утки {cls.color}')

    def __repr__(self): # Вывод строк
        return f'Имя утки: {self.name}, вес {self.weight} кг.'

    def __lt__(self, other): # принимающий 2х уток, и возвращающий имя более тяжелой утки (меньше чем)
        if self.weight < other.weight:
            return f'Утка {other.name}, тяжелее'
        else:
            return f'Утка {self.name}, тяжелее'

    def __ne__(self, other): # метод, сравнивающий вес 2х уток и возвращающий bool (равен вес или нет)
        return self.weight != other.weight

    def __add__(self, other): # , суммирующий вес 2х уток
        return self.weight + other.weight

duck_1 = Duck('Серай шейка', 4)
duck_2 = Duck('Гадкий утенок', 1)
duck_3 = Duck('Зигзаг Маккряк', 85)

duck_1.crack()
duck_3.duck_color()
print(duck_2)
print(duck_1 < duck_3)
print(duck_3 != duck_2)
print(f'Общий вес уток: {duck_1 + duck_2} кг.')
