import random


input_data = input("Введите нижнюю и верхнюю границы через пробел: ")
numbers = sorted([int(i) for i in input_data.split(" ")])[:2]
guess_number = random.randint(*numbers)

while True:
    x = input("Попробуй отгадать моё число ")
    if not x.isdecimal():
        break
    x = int(x)
    if x > guess_number:
        print("Загаданное число меньше ")
    elif x < guess_number:
        print("Загаданное число больше ")
    else:
        print("Вы угадали!")
        break
