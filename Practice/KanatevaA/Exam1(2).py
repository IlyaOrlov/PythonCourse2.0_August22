#Написать реализацию встроенной функции len: функция принимает список, возвращает его длину.
#Стандартную функцию len использовать нельзя!

def myfun(l):
    len(l)
    return len(l)

print(myfun("kdkfkbkjbkjbf"))

#Написать реализацию функции reversed:
#функция принимает список, возвращает этот же список,
#располагая элементы в обратном порядке. Стандартную функцию reversed и метод reverse использовать нельзя! (4 балла)


#l = ("sbjbss")
#for i in l[::-1]:
#    print(i)


#def myfun(a):
#    for i in a[::-1]:
#        return i
#        print(myfun(fjflg))
def myfun(a):
    for i in a[::-1]:
        return a           #исправила return что-бы фраза выводилась певернутая целиком
print(myfun("fjflg"))

