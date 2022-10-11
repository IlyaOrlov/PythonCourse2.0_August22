import itertools

t = ([1, 2, 3], [4, 5], [6, 7])
lst = []
f = itertools.chain(t)
for i in f:
    lst += i
print(lst)

c = ['hello', 'i', 'write', 'cool', 'code']
l = itertools.filterfalse(lambda x: len(x) < 5, c)
lst1 = list(l)
print(lst1)

d = 'password'
v = itertools.combinations_with_replacement(d, 4)
print(list(v))

