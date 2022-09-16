word = ["Ты сам-то понял, что написал?", "Аргументируй", "И?"]
i = -1
while True:
    a = input()
    if a == "":
        print("Чего молчишь? Сказать нечего?")
        continue
    elif a.lower() == "хватит":
        print("Ну хватит - так хватит, чего кричать-то?")
        break
    if i > 2:
        i = 0
    else:
        i += 1
    print(word[i])
