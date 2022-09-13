a = int(input("Введите а: "))
b = int(input("Введите b: "))

def fun(a, b):
    last = 0
    if a > b:
        last = a
        print(f"Наибольшее a: {last}")
    elif b > a:
        last = b
        print(f"Наибольшее b: {last}")

fun(a,b)