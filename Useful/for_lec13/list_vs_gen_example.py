a = [x for x in range(100) if x % 2 == 0]
b = (x for x in range(100) if x % 2 == 0)

print(a)
print(next(b))
print(next(b))
print(next(b))


