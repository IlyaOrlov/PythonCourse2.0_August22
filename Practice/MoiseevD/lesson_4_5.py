import random


s = int(input('Введите нижний диапазон: '))
s1 = int(input('Введите верхний диапазон: '))
num = random.randint(s, s1)

while True:
    guess_str = input('Угадайте число: ')
    if not guess_str.isdecimal():
        print('---Завершение---')
        break
    guess = int(guess_str)
    if guess == num:
        print('---Вы угадали---')
        break
    elif guess < num:
        print('   Ваше число меньше ')
    elif guess > num:
        print('   Ваше число больше ')
