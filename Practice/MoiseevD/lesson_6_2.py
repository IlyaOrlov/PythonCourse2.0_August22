class Duck:
    def __init__(self, name, weight, collor):
        self._name = name
        self._weight = weight
        self._collor = collor

    def name_weight(self):
        print('Имя:', self._name, '     Вес:', self._weight, 'кг')

    def __repr__(self):
        return f'class Duck: name = {self._name}   weight = {self._weight}   collor = {self._collor}'

    def __lt__(self, other):
            if self._weight < other._weight:
                return other._name
            else:
                return self._name

    def __ne__(self, other):
            return self._weight != other._weight

    def __add__(self, other):
            return self._weight + other._weight

    @classmethod
    def collor_duck(cls, collor):
        print(cls, collor)

    @staticmethod
    def crack_duck():
        print('Crack')


p = Duck('Гага', 4, 'белый',)
p1 = Duck('КряКря', 7, 'черный',)

p.crack_duck()
p.collor_duck('черный')
p.name_weight()
print(repr(p))
print(repr(p1))
print('Самая тяжелая утка: ', p < p1)
print('Вес уток не равен: ', p != p1)
print('Общий вес уток: ', p + p1)
