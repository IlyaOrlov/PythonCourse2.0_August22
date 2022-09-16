i = input("Введите пятизначное число: ")
count = 0
print(f"Число: {i}")

for n in i:
    count += 1
    print(f"{count} цифра равна {n}")
