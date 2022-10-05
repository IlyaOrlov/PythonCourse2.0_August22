import itertools


x = itertools.chain([1, 2, 3], [4, 5], [6, 7])
print(*x)

x = itertools.filterfalse(lambda x: len(x) < 5, ['hello', 'i', 'write', 'cool', 'code'])
print(*x)

str = 'password'
x = itertools.combinations(str, 4)
print(*x)