arr = [0, 3, 24, 2, 3, 7]

for i in range(len(arr)):
    for m in range(i, len(arr)):
        if arr[i] > arr[m]:
            arr[i], arr[m] = arr[m], arr[i]
print(arr)

