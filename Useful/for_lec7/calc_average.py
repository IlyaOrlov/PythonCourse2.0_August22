lst = [2, 4, 5, 7, "hello", 10]
# найти сред. ариф. чисел из этого списка
# type(lst[i]) is int:
# isinstance(lst[i], int)
# (1 + 5 + 7)/3

average = sum((x := [n for n in lst if type(n) is int]))/len(x)
print(average)

lst = [2, 4, 5, 7, "hello", 10]
sum = 0
count = 0
for i in range(len(lst)):
    if type(lst[i]) is int:
        sum += lst[i]
        count += 1
print(f'{sum / count}')


average = 0
count = 0
for i in lst:
    if type(i) is int:
        average += i
        count += 1
average = average / count
print(average)
