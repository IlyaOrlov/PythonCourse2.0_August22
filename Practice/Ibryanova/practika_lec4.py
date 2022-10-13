def find_first_num(s):
    return next(i for i in s if i.isdecimal())


s1 = input("Введите строку: ") # dfkg2sfhg6fdg3 -> 2
s2 = "abcd5kkk6" #5
# нужно чтобы ф-я вернула первый числовой символ в s1 и s2
print(find_first_num(s1))
print(find_first_num(s2))


#s = "x1gfh2fg5fg7"       эту ф-ю можно записать иначе  s = "x1gfh2fg5fg7"
#lst = []                 lst = [i for i in s if not i.isdecimal()]
#for i in s:               print(lst)
#   if not i.isdecimal():
#        lst.append(i)
#print(lst)
#
#
#
#
#
