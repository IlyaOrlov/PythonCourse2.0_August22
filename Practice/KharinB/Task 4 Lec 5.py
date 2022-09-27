def fun(arr, x):
    y = set()  # Создал сразу множество
    for i in arr:
        if x in i:
            for j in range(len(i)):
                if i[j] == x:
                    y.add(j)
    if y != set():
        y = list(y)
        y.sort(reverse=True)
        for c in y:
            for g in arr:
                g.pop(c)
    return None



matrix = input("Введите матрицу: ") or [["a", 3, 6], [3, 7, 5], [0, 5, 3]]
x = input("Введите символ: ") or "3"
if x.isdecimal():
    x = int(x)
a = fun(matrix, x)
print(matrix)
