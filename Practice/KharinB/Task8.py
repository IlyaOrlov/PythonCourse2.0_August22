import random

while True:
    player = input("Введите количество игроков, помимо Вас: ")
    if player.isdecimal():
        player = int(player)
        if player < 1:
            print("Игроков слишком мало.")
        elif player > 4:
            print("Игроков слишком много.")
        else:
            break
    else:
        print("Введено не число, повторите ввод.")

flag = True
while flag:
    while True:
        answer = input("Выберете камень(к), ножницы(н) или бумагу(б)").lower()
        if answer == "к":
            range_game = ["ножницы", "камень", "бумага"]
            break
        elif answer == "н":
            range_game = ["бумага", "ножницы", "камень"]
            break
        elif answer == "б":
            range_game = ["камень", "бумага", "ножницы", ]
            break
        else:
            print("Выбор непонятен.")
    result = [0, 0, 0]
    for i in range(player):
        ans_pl = random.randint(0, 2)
        print(f"{i + 2} игрок выкинул: {range_game[ans_pl]}")
        result[ans_pl] += 1
    if result[0] == 0 and result[2] > 0:
        print("Вы проиграли")
        break
    elif result[2] == 0 and result[1] == 0:
        print("Вы выиграли")
        break
    elif result[2] != 0 and result[0] != 0:
        print("Куча-мала, переброс.")
    elif result[1] > 1:
        print(f"{result[0]} игроков выбывает! Следующий раунд!")
        player -= result[0]
