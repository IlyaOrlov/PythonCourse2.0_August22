a = int(input("Введите а: "))
b = int(input("Введите b: "))

def fun(a, b):
    if a > b:
        print(f"Наибольшее a: {a}")
        return a
    elif b > a:
        print(f"Наибольшее b: {b}")
        return b

fun(a,b)