import random

range = input("Введите диапазон чисел: ").split()
hidden_numbers = random.randint(int(range[0]), int(range[1]))
numbers_1 = input("Угадайте целое число: ")
while True:
    if not numbers_1.isdigit():
        print("Вы ввели нечисловой символ")
        break
    else:
        numbers_1 = int(numbers_1)
        if numbers_1 < hidden_numbers:
            print("Загаданное число больше введенного")
        elif numbers_1 > hidden_numbers:
            print("Загаданное число меньше введенного")
        else:
            print("Вы угадали")
            break
    numbers_1 = input("Угадайте целое число: ")




