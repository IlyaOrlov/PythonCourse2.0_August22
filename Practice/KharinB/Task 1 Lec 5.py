arr = [0, 3, 0, 24, 2, 3, 8, 6, 8, 78, 8, 7]
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)
