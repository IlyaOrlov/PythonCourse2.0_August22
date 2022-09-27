def fun(lst):
    for i in range(len(lst)):
        min = i
        for x in range(i + 1, len(lst)):
            if lst[x] < lst[min]:
                min = x
        if i != min:
            lst[i], lst[min] = lst[min], lst[i]


arr = [0, 3, 24, 2, 3, 7]
res = fun(arr)
print(f"Отсортированный список: {arr}")