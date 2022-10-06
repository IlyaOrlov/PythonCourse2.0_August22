lst = [1, 2, 3, 4, 5, 6]
for i in lst:
    if i % 2 == 0:
        print(i)
        break


print([i for i in lst if i % 2 == 0][0])

print(next((i for i in lst if i % 2 == 0), None))
