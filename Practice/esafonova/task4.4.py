lis = ["Ты сам-то понял, что написал?", "Аргументируй", "И?"]
count = 0

while True:
    n = input("Ваш запрос: ")
    count += 1
    if count > len(lis):
        count = 1
    elif n == "хватит":
        break
    print(lis[count - 1])




