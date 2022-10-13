#вернула вызов функции (случайно его снесла вместе с res и не проверила)
def fun(lst):
    for i in range(len(lst)):
        minimal = i
        for x in range(i + 1, len(lst)):
            if lst[x] < lst[minimal]:
                minimal = x
        if i != minimal:
            lst[i], lst[minimal] = lst[minimal], lst[i]


arr = [0, 3, 24, 2, 3, 7]
fun(arr)
print(f"Отсортированный список: {arr}")