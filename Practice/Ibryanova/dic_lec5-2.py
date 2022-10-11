#s = {'dog', 'four', 'table'}
#s1 = frozenset({1, 2, 3})
#s.add(s1)# s.addfrozenset((s1))
#print(s)


#lst = [1, 2, 3, 1, 2]
#f = frozenset(lst)
#lst = list(f)
#print(lst)




# определение уникальных значений которые ввел пол=ль
s = set()
while True:
    i = input('введите что - нибудь: ')
    if i == 'stop':
        break
    s.add(i)


print(s)


