import random


game_list = ("камень", "ножницы", "бумага")

while True:
    game = random.choice(game_list)
    s = input('Введите слово "КАМЕНЬ", "НОЖНИЦЫ", или "БУМАГА": ')
    if s.lower() == 'камень':
        if game == game_list[0]:
            print(f'---{game}---\n Ничья')
    if s.lower() == 'камень':
        if game == game_list[1]:
            print(f'---{game}---\n Вы выиграли')
    if s.lower() == 'камень':
        if game == game_list[2]:
            print(f'---{game}---\n Вы проиграли')

    if s.lower() == 'ножницы':
        if game == game_list[0]:
            print(f'---{game}---\n Вы проиграли')
    if s.lower() == 'ножницы':
        if game == game_list[1]:
            print(f'---{game}---\n Ничья')
    if s.lower() == 'ножницы':
        if game == game_list[2]:
            print(f'---{game}---\n Вы выиграли')

    if s.lower() == 'бумага':
        if game == game_list[0]:
            print(f'---{game}---\n Вы выиграли')
    if s.lower() == 'бумага':
        if game == game_list[1]:
            print(f'---{game}---\n Вы проиграли')
    if s.lower() == 'бумага':
        if game == game_list[2]:
            print(f'---{game}---\n Ничья')