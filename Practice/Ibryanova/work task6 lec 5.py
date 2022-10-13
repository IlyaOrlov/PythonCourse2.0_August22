# задание - из списка найти все числа и посчитать их ср ариф
lst = [2, 4, 5, 7, 'hello', 10]
#type(lst[i]) is int:
#isinstance(lst[i], int)

average = sum((x := [n for n in lst if type(n) is int]))/len(x)
print(average)

lst = [2, 4, 5, 7, 'hello', 10]
sum = 0
count = 0
for i in range(len(lst)):
    if type(lst[i]) is int:
        sum += lst[i]
        count += 1
print(f'{sum / count}')
