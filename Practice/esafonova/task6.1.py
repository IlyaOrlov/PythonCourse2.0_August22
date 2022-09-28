# Спроектировать классы (один или несколько) для игры в танки и создать экземпляры этих классов.
class Tank:
    def __init__(self, name, model, power):
        self.name = name
        self.model = model
        self.power = power

    def show(self):
        print(f'Игрок: {self.name} с танком {self.model} и мощностью {self.power}')

    def __lt__(self, other):
        if self.power > other.power:
            return f'У Игрока {self.name} больше шансов'
        elif self.power == other.power:
            return 'Шансы равны'
        else:
            return f'У Игрока {self.name} меньше шансов'

    def __str__(self):
        return  f'Игрок: {self.name} с танком {self.model} и мощностью {self.power}'

    def __repr__(self):
        return f'Игрок: {self.name} с танком {self.model} и мощностью {self.power}'


player1 = Tank('Вася', 'Т-34', 400)
player2 = Tank('Игорь', 'Т-54', 382)
lst = [player1, player2]
print('Добро пожаловать в игру!')
for i in lst:
    i.show()
print(player1 < player2)
print('Да начнется, игра!')