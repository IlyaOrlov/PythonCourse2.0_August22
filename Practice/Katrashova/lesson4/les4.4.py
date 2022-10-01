import random


t = ("Ты сам-то понял, что написал?", "Аргументируй", "И?")
a = "хватит"

while True:
    i = input("Введите запрос: ")
    if i == a:
        break
    else:
        print(random.choice(t))