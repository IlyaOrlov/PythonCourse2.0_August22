def max_num(a, b):
    return a if a > b else b


a = int(input('Введите целое число x: '))
b = int(input('Введите целое число y: '))
res = max_num(a, b)
print(res)


#x = int(input('Введите целое число x: '))
#y = int(input('Введите целое число y: '))
#f = lambda a, b: a if a > b else b
#print(f(x, y))

def max_num2(a, b):
    if a > b:
        print(a)
    else:
        print(b)

a = int(input('Введите целое число x: '))
b = int(input('Введите целое число y: '))
res = max_num2(a, b)
print(res)