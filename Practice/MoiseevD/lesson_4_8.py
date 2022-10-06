import random


game_list = ("камень", "ножницы", "бумага")

while True:
    game = random.choice(game_list)
    s = input('Введите слово "КАМЕНЬ", "НОЖНИЦЫ", или "БУМАГА": ')
    s = s.lower()
    if s == 'камень':
        if game == game_list[0]:
            print(f'---{game}---\n Ничья')
        elif game == game_list[1]:
            print(f'---{game}---\n Вы выиграли')
        else:
            print(f'---{game}---\n Вы проиграли')

    elif s == 'ножницы':
        if game == game_list[0]:
            print(f'---{game}---\n Вы проиграли')
        elif game == game_list[1]:
            print(f'---{game}---\n Ничья')
        else:
            print(f'---{game}---\n Вы выиграли')

    elif s.lower() == 'бумага':
        if game == game_list[0]:
            print(f'---{game}---\n Вы выиграли')
        elif game == game_list[1]:
            print(f'---{game}---\n Вы проиграли')
        else:
            print(f'---{game}---\n Ничья')