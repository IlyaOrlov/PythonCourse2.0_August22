import random


a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
print(f"Диапазон для загадывания числа: от {a} до {b}")
number = random.randint(a, b)
while True:
    guess = int(input("Введите целое число из заданного диапазона: "))
    if guess == number:
        print("Поздравляю! Вы угадали!")
        break
    elif guess  < number:
        print("Нет заданное число больше этого. Попробуйте еще раз!")
    else:
        print("Нет, загаданное число меньше этого. Попробуйте еще раз!")