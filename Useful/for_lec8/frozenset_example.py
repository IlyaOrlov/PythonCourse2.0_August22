s = {"dog", "four", "table"}
s1 = frozenset({1, 2, 3})
s.add(s1)
print(s)

lst = [1, 2, 3, 1, 2]
f = frozenset(lst)
lst = list(f)
print(lst)
