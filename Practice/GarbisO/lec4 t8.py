import random


actions = ("камень", "ножницы", "бумага")
gamer_action = " "
while True:
    gamer_action = input("Сделайте выбор (камень, ножницы или бумага): ")
    computer_action = random.choice(actions)
    print(f"Ваш выбор: {gamer_action}, выбор компьютера: {computer_action}")
    if gamer_action == computer_action:
        print("Ничья!")
    elif gamer_action == "камень":
        if computer_action == "бумага":
            print("Бумага оборачивает камень. Вы проиграли...")
        else:
            print("Камень ломает ножницы. Вы победили!")
    elif gamer_action == "ножницы":
        if computer_action == "бумага":
            print("Ножницы режут бумагу. Вы победили!")
        else:
            print("Камень ломает ножницы. Вы проиграли...")
    elif gamer_action == "бумага":
        if computer_action == "ножницы":
            print("Ножницы режут бумагу. Вы проиграли...")
        else:
            print("Бумага оборачивает камень. Вы победили!")
