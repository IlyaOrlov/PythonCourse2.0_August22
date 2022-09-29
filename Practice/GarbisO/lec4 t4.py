import random


request = " "
answers = ("Ты сам-то понял что написал?", "Аргументируй", "И?")
while True:
    request = input("Введите запрос: ")
    if request == "хватит":
        print("До свидания!")
        break
    else:
        n = random.choice(answers)
        print(n)



