lst1 = [1, 23, "abc", "efg", [1, 2, 3]]
lst2 = lst1
lst1.append(1000)
print(lst1)
print(lst2)

s = "1234567"
lst = list(s)
print(lst)
s1 = "+".join(lst)
print(s1)
lst = s1.split("+")
print(lst)