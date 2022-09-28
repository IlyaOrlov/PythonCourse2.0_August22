import random


# lst = [random.randint(1, 100) for _ in range(100)]

lst = []
for _ in range(100):
    lst.append(random.randint(1, 100))

print(lst)
lst = list(set(lst))
print(lst)
