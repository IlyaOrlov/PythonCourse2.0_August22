# Task 2
# Для человека привычнее в километрах.
distace = int(input('Введите расстояние в километрах: '))
# почему в минутах? потому, что человеку проще посчтить время в минутах, чем в десятках.
time = int(input('Введите время в пути в минутах: '))
# Переводим минуты в часы
hour = time / 60
# Расчет средней скорости/ так как в условиях задачи нет условия о формате, ставлю int() для вывода целого числа
speed = int(distace / hour)
print(f'Средняя скорость движения {speed} км/ч')

# Второй вариант решения
lang = input('Выберите язык / Сhoose the language: rus / eng: ')
if lang == 'rus':
    distace = int(input('Введите расстояние в километрах: '))
    time = int(input('Введите время в пути в минутах: '))
    hour = time / 60
    speed = int(distace / hour)
    print(f'Средняя скорость движения {speed} км/ч')
else:
    distace = int(input('Enter the distance in miles: '))
    time = int(input('Enter the travel time in minutes: '))
    hour = time / 60
    speed = int(distace / hour)
    print(f'Average speed of movement {speed} mph')