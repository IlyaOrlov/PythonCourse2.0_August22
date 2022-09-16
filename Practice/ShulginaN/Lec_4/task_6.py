def max_number(a, b):
    if a > b:
        print(a)
    else:
        print(b)


x = input("Введите 'a': ")
y = input("Введите 'b': ")
max_number(x, y)


def max_number2(a, b):
    return a if a > b else b


m = input("Введите 'a': ")
n = input("Введите 'b': ")
res = max_number2(m, n)
print(res)
