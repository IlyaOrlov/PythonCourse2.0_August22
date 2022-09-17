def fun(arr, x):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == x:
                for n in range(len(arr)):
                    arr[n].pop(j)
                break
    return None


matrix = input("Введите матрицу: ") or [["a", 3, 7], [3, 4, 5], [4, 5, 6]]
x = input("Введите символ: ")
if x.isdecimal():
    x = int(x)
a = fun(matrix, x)
print(matrix)
