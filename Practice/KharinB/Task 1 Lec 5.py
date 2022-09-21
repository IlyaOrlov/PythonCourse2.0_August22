arr = [0, 3, 0, 24, 2, 3, 8, 6, 8, 78, 8, 7]
arr = list(enumerate(arr, 0))
for i in range(len(arr)):
    x = arr[i::]
    y = min(x, key=lambda i: i[1])[0]
    arr[y], arr[i] = (arr[y][0], arr[i][1]), arr[y][1]
print(arr)

# Я конечно решил задачу 4.2 не так, но намёк понял)))
