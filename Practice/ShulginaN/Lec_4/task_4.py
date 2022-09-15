import random


t = ("Ты сам-то понял, что написал?", "Аргументируй", "И?")
x = "хватит"

while True:
    i = input("Напиши мне что-то: ")
    if i == x:
        break
    else:
        print(random.choice(t))
