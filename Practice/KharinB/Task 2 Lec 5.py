arr = input("Введите массив:", ) or [2, 3, 4, 5, 3, 2]
for i in range(len(arr)):
    if arr[i::][0] in arr[:i:]:
        print(arr[i])
        break
