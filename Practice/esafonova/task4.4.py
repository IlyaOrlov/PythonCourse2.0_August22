lis = ["Ты сам-то понял, что написал?", "Аргументируй", "И?"]
count = 0

while True:
    n = input("Ваш запрос: ")
    count += 1
    if n == "хватит":
        break
    elif count == 2:
        print(lis[1])
        continue
    elif count == 3:
        count = 0
        print(lis[2])
        continue
    else:
        print(lis[0])

