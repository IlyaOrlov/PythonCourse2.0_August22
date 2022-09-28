import random


answer = ("Ты сам-то понял, что написал?", "Аргументируй", "И?")
signal = "хватит"

while True:
    a = input("Задайте вопрос: ")
    if a == signal:
        break
    else:
        print(random.choice(answer))
print("Завершено")
