import random


def fun(c):
    c = c.lower()
    if c == 'y':
        return True
    else:
        print('Как скажете.')
        return False


print('Привет! Давай сыграем в: "Камень", "Ножницы", "Бумага"? ')

while True:
    a = int(input('Сделайте ваш выбор: 1 - Камень 2 - Ножницы 3 - Бумага: '))
    b = random.randrange(1, 4)

    if a == 1:
        print('Вы выбрали: Камень')
    elif a == 2:
        print('Вы выбрали: Ножницы')
    else:
        print('Вы выбрали: Бумагу')

    if b == 1:
        print('Противник выбрал: Камень')
    elif b == 2:
        print('Противник выбрал: Ножницы')
    else:
        print('Противник выбрал: Бумагу')

    if a == b:
        print('Ничья.')
    elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
        print('Поздравляю! Вы победили!')
    else:
        print('Сожалеем. Вы проиграли.')
    c = input('Сыграете еще? y/n: ')
    if fun(c):
        continue
    else:
        break
