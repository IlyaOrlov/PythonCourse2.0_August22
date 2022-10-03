arr = [0, 3, 24, 2, 3, 7]

for i in range(len(arr)):
    m = i
    for a in range(i + 1, len(arr)):
        if arr[a] < arr[m]:
            m = a
    if i != m:
        arr[i], arr[m] = arr[m], arr[i]
print(arr)
