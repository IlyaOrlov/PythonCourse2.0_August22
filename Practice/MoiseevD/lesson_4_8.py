import random


game_list = ["камень", "ножницы", "бумага"]
game = random.choice(game_list)

while True:
    s = input('Введите слово "КАМЕНЬ", "НОЖНИЦЫ", или "БУМАГА": ')
    if s.lower() == 'камень' and game == game_list[0]:
        print(f'---{game}---\n Ничья')
    elif s.lower() == 'камень' and game == game_list[1]:
        print(f'---{game}---\n Вы выиграли')
    elif s.lower() == 'камень' and game == game_list[2]:
        print(f'---{game}---\n Вы проиграли')

    elif s.lower() == 'ножницы' and game == game_list[0]:
        print(f'---{game}---\n Вы проиграли')
    elif s.lower() == 'ножницы' and game == game_list[1]:
        print(f'---{game}---\n Ничья')
    elif s.lower() == 'ножницы' and game == game_list[2]:
        print(f'---{game}---\n Вы выиграли')

    elif s.lower() == 'бумага' and game == game_list[0]:
        print(f'---{game}---\n Вы выиграли')
    elif s.lower() == 'бумага' and game == game_list[1]:
        print(f'---{game}---\n Вы проиграли')
    elif s.lower() == 'бумага' and game == game_list[2]:
        print(f'---{game}---\n Ничья')