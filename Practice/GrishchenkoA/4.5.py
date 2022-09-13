import random

range = input("Введите диапазон чисел: ").split()
hidden_numbers = random.randint(int(range[0]), int(range[1]))
numbers_1 = input("Угадайте целое число: ")
if numbers_1.isdigit():
    while int(numbers_1) != int(hidden_numbers):
            if int(numbers_1) < hidden_numbers:
                print("Загаданное число больше введенного")
                numbers_1 = input("Угадайте целое число: ")
            elif int(numbers_1) > hidden_numbers:
                print("Загаданное число меньше введенного")
                numbers_1 = input("Угадайте целое число: ")
    print("Вы угадали")
else:
    print("Вы ввели нечисловой символ")



