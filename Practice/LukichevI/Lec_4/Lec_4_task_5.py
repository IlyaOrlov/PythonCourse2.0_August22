import random

while True:
    a = input('Введите начальное число диапазона: ')
    if not a.isdecimal():
        print('Вы ввели не число')
        continue
    b = input('Введите конечное число диапазона: ')
    if not b.isdecimal():
        print('Вы ввели не число')
        continue
    if a.isdecimal() and b.isdecimal():
        break
a = int(a)
b = int(b)
c = random.randint(a, b)
print('Я загадал число в указанном диапазоне')
while True:
    d = input('Введите угадываемое число: ')
    if not d.isdecimal():
        print('Вы ввели не число')
        continue
    d = int(d)
    if c < d:
        print('Число чуть меньше, попробуй еще')
    elif c > d:
        print('Число чуть больше, попробуй еще')
    else:
        print('Браво, Вы угадали, купите лотерейный билетик 8)')
        break