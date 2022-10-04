lst = [1, 2, 3]
a = [x * 2 for x in lst]
b = (x * 2 for x in lst)

print(type(a))
print(type(b))

print(a)
print(b)
for i in b:
    print(i)