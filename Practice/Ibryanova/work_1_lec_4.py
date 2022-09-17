a = 30
b = 20
if b > a:
    print(b)
else:
    print(a)

r = (b, a)
print(f"{r[0]=}")
print(f"{r[1]=}")
#a > b =>True -> 1
#False -> 0
#print ([a > b]) # a
# (b, a) [a > b]


# строку можно привести к типу число с помощью методов, например,
distance = input("Введите число: ")
if distance.isdecimal():# есть еще методы isdigit():  и isnumeric():
    print(distance)
else:
    print("Введено не число!")