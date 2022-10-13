#lst = ['1', '2', 'abc', '4', 'in']
#lst_new = [int(i)**2 for i in lst if i.isdecimal()]
#print(lst_new)

# сгенирировать послед -ть чисел
#count = 0
#lst_nums = []
#while count < 10:
#   lst_nums.append(count)
#   count += 1
#print(lst_nums)


# st_nums = []
# #lst_nums = [i for i in range(10)] списковое выражение
# for i in range(10):
#    lst_nums.append(i)
# print(lst_nums)

lst = ['1', '2', 'abc', '4', 'in'] # вместо range можно испол-ть enumerate
for idx, el in enumerate(lst):
    print(f'{idx} - {el}')

t = 1, 2
print(type(t))
a, b = t
print(f'{a=}, {b=}')



