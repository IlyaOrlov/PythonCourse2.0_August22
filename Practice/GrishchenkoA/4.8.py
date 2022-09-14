import random

play = ["камень", "ножницы", "бумага"]
while (player_1 := input("Введите ваш вариант: ").lower()) != "хватит":
    player_2 = random.choice(play)
    print(f"Вариант компьютера: {player_2}")
    if player_1 == "камень":
        if player_2 == "камень":
            print("Ничья")
        elif player_2 == "ножницы":
            print("Вы выиграли")
        elif player_2 == "бумага":
            print("Вы проиграли")
    elif player_1 == "ножницы":

        if player_2 == "камень":
            print("Вы проиграли")
        elif player_2 == "ножницы":
            print("Ничья")
        elif player_2 == "бумага":
            print("Вы выиграли")
    elif player_1 == "бумага":

        if player_2 == "камень":
            print("Вы выиграли")
        elif player_2 == "ножницы":
            print("Вы проиграли")
        elif player_2 == "бумага":
            print("Ничья")