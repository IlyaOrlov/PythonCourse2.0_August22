def fun():
    '''
    Эта функция возвращает значение 10
    '''

    return 10

print(fun.__doc__)
x = input("Введите число: ")
print(x)
y = input("Введите число: ")
print(y)
summ = x + y
result = summ % 2
print (f"Остаток от деления на 2: {result}")
print("the end")