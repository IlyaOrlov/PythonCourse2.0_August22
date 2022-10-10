# написать свою реализацию random.choice
import random


def ch(arr):
    return arr[random.randint(0, len(arr)-1)]

print(ch([1, 2, 3, 4]))

lst = ('Иванов', 'Петров', 'Сидоров', 'Сидоров', 'Сидоров', 'Петров', 'Петров' )
# найти только повторяющихся сотрудников 'Петров', 'Сидоров'
s = set()
pov = set()
for i in lst:
    if i in s:
        pov.add(i)
    else:
        s.add(i)
print(pov)



s = list()
pov = list()
for i in lst:
    if i in s:
        pov.append(i)
    else:
        s.append(i)
print(pov)







