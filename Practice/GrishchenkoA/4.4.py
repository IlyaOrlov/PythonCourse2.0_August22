import random

answer = ["Ты сам-то понял, что написал?", "Аргументируй", "И?"]
while (request := input("Введите запрос: ")) != "хватит":
    print(random.choice(answer))