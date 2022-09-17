number = input("Введите 5-ое число: ")

def numbers(n):
    count = 1
    for i in n:
        print(f"{count} цифра равна {i}")
        count += 1

numbers(number)