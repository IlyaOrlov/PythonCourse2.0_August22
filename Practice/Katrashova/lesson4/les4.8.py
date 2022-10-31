import random

print("Давай сыграем в камень, ножницы, бумага")
x = ("камень", "ножницы", "бумага")

while True:
    y = input("Твой выбор - камень, ножницы, бумага: ")
    comp = random.choice(x)
    print(f"Вы выбрали {y}, компьютер выбрал {comp}.")
    if y == comp:
        print("Ничья!")
    elif y == "камень":
        if comp == "ножницы":
            print("Ты победил!")
        else:
            print("Ты проиграл.")
    elif y == "бумага":
        if comp == "камень":
            print("Ты победил!")
        else:
            print("Ты проиграл.")
    elif y == "ножницы":
        if comp == "бумага":
            print("Ты победил!")
        else:
            print("Ты проиграл.")