def find_max(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        print("Числа равны")
x = int(input("Введите число a: "))
y = int(input("Введите число b: "))
res = find_max(x, y)
print(f"Большее число: {res}")


def print_max(a, b):
    if a > b:
        print(a)
    elif a < b:
        print(b)
    else:
        print("Числа равны")
x = int(input("Введите число a: "))
y = int(input("Введите число b: "))
print_max(x, y)
