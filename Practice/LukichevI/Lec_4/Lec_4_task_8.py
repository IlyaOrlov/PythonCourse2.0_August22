import random

print('Привет! Давай сыграем в: "Камень", "Ножницы", "Бумага"? ')

while True:

    a = int(input('Сделайте ваш выбор: 1 - Камень 2 - Ножницы 3 - Бумага: '))
    b = random.randrange(1, 4)
    print(b)

    if a == 1:
        print('Вы выбрали Камень')
    elif a == 2:
        print('Вы выбрали Ножницы')
    else:
        print('Вы выбрали Бумагу')

    if b == 1:
        print('Противник выбрали Камень')
    elif b == 2:
        print('Противник выбрали Ножницы')
    else:
        print('Противник выбрал Бумагу')

    if (a == 1 and b == 1) or (a == 2 and b == 2) or (a == 3 and b == 3):
        print('Ничья.')
        c = input('Сыграете еще? y/n: ')
        c = c.lower()
        if c == 'y':
            continue
        else:
            print('Как скажете.')
            break
    elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
        print('Поздравляю! Вы победили!')
        c = input('Сыграете еще? y/n: ')
        c = c.lower()
        if c == 'y':
            continue
        else:
            print('Как скажете.')
            break
    else:
        print('Сожалею. Вы проирали.')
        c = input('Сыграете еще? y/n: ')
        c = c.lower()
        if c == 'y':
            continue
        else:
            print('Как скажете.')
            break