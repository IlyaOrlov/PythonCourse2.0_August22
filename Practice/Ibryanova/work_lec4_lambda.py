# нужно сравнить два числа, кот-е вводит пол-ль  и напишем
# фун=ю, кот-я возводит в кв наибольшее число
def find_max(a, b):
    return a if a > b else b # выражение условия if  else = можно записать в одну строку

#    if a > b:
#        return a
#    else:
#        return b

x =int(input("input x: "))
y =int(input("input y: "))
f = lambda  a, b: a if a > b else b # с помощью lambda мы сократили запись фун-и find_max
res = f(x, y) ** 2
print(res)

