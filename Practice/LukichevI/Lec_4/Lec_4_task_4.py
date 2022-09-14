import random

a = ["Ты сам-то понял, что написал?", "Аргументируй", "И?"]
while True:
    b = input("Введите вопрос: ")
    if b.lower() == "хватит":
        print('Ни кто тебя не схватит 8)')
        break
    c = random.choice(a)
    print(c)
