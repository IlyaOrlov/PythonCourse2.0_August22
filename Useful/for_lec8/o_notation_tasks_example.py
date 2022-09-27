# Написать свою реализацию random.choice
import random

def ch(arr):
    return arr[random.randint(0, len(arr)-1)]

print(ch([1, 2, 3, 4]))

# Найти только повторяющихся сотрудников
# "Петров", "Сидоров"
# O(1) O(logN) O(N) O(N^2) O(N!)

lst = ("Иванов", "Петров", "Сидоров", "Сидоров", "Петров", "Петров")
s = set()
pov = set()
for i in lst:  # O(N) * O(1) * O(1) => O(N)
    if i in s:  # O(1)
        pov.add(i)  # O(1)
    else:
        s.add(i)  # O(1)
print(pov)


s = list()
pov = list()
for i in lst:  # O(N): O(N) * O(N) => O(N^2)
    if i in s:  # O(N)
        pov.append(i)  # O(1)
    else:
        s.append(i)  # O(1)
print(pov)


lst1 = [i for i in set(lst) if lst.count(i) > 1]
# set(lst) => O(N) + (O(N) * O(N)) => O(N) + O(N^2) => O(N^2)
# lst.count(i): O(N)
print(lst1)
