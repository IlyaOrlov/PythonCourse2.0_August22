# Спроектировать классы (один или несколько) для игры в танки и создать экземпляры этих классов.
class Tank:
    def __init__(self, name, model, power):
        self._name = name
        self._model = model
        self._power = power

    def show(self):
        print(f'Игрок: {self._name} с танком {self._model} и мощностью {self._power}')

    def __lt__(self, other):
        if self._power > other._power:
            return f'У Игрока {self._name} больше шансов'
        elif self._power == other._power:
            return 'Шансы равны'
        else:
            return f'У Игрока {self._name} меньше шансов'

    def __str__(self):
        return  f'Игрок: {self._name} с танком {self._model} и мощностью {self._power}'

    def __repr__(self):
        return f'Игрок: {self._name} с танком {self._model} и мощностью {self._power}'


player1 = Tank('Вася', 'Т-34', 400)
player2 = Tank('Игорь', 'Т-54', 382)
lst = [player1, player2]
print('Добро пожаловать в игру!')
for i in lst:
    i.show()
print(player1 < player2)
print('Да начнется, игра!')