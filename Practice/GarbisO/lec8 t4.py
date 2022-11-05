import itertools


lst = ([1, 2, 3], [4, 5], [6, 7])
res = list(itertools.chain.from_iterable(lst))
print(res)

lst1 = (['hello', 'i', 'write', 'cool', 'code'])
res1 = list(itertools.filterfalse(lambda x: len(x) < 5, lst1))
print(res1)

res2 = list(itertools.combinations("password", 4))
print(res2)
