lst = {1, 2, 3, 4}

# for i in lst:
#     print(i)

it = iter(lst)
try:
    while True:
        i = next(it)
        print(i)
except StopIteration:
    pass



