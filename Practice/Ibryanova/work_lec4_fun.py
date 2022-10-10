#def cheсk_num(num):
#   pass# заглушка


#x = input('введите число: ')
#r_max = cheсk_num(x)
#x = input('введите число: ')
#r_min = cheсk_num(x)




# напишем ф-цию, которая сможет принять любое кол-во эл-ов
#def fun(*args):
#   m = 0
#    for i in args:
#        m += i
#    return m

#res = fun(10, 20, 30, 40)
#print(res)
#если мы хотим передать не 2 числа, а больше, то испол-т оператор
# *args = собирает в набор позиционные арг-ты



#есть оператор **kwargs = собирает в набор именованные арг-ты
def fun(x, y, *args, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)
    m = 0
    for i in args:
        m += i
    return m

res = fun(10, 20, 30, 40, a=30, b=10)
print(res)