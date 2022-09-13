numbers = input("Введите пятизначное число: ")
for i, d in enumerate(numbers):
    print(f"{i+1} цифра равна {int(d)}")