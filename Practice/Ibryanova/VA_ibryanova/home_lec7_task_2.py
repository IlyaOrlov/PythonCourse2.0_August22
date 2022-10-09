class Duck:
    color = 'Серый'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @staticmethod
    def crack_metod():
        print('Сrack')

    @classmethod
    def color_metod(a):
        print(f'{a.color}')

    def __repr__(self):
        return f'Имя: {self.name} вес: {self.weight} кг'

    def __lt__(self, other):
        if self.weight < other.weight:
            return f'{other.name} тяжелее'
        else:
            return f'{self.name} тяжелее'

    def __ne__(self, other):
        return self.weight != other.weight


    def __add__(self, other):
        return self.weight + other.weight



duck1 = Duck('Вилли', 3)
duck2 = Duck('Дилли', 4)
duck3 = Duck('Билли', 5)


Duck.crack_metod()
Duck.color_metod()
print(duck1)
print(duck2)
print(duck3)
print(duck1 > duck3)
print(duck2 != duck3)
print(f'Вес двух уток составит: {duck1 + duck3} кг')
