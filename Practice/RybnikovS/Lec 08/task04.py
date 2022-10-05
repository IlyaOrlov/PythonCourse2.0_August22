import itertools


x = itertools.chain([1, 2, 3], [4, 5], [6, 7])
print(*x)

x = itertools.filterfalse(lambda x: len(x) < 5, ['hello', 'i', 'write', 'cool', 'code'])
print(*x)
# Функция выдает на строку 'password' все возможные комбинации вида ([('p', 'a', 's', 's'), ('p', 'a', 's', 'w'), ('p', 'a', 's', 'o'), ...)
str = 'password'
x = itertools.combinations(str, 4)
print(*x)