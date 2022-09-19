arr = [0, 3, 24, 2, 3, 7]
for i in range(0, len(arr)):
    a = min(arr[i:])
    c = arr.index(a, i)
    arr[c], arr[i] = arr[i], arr[c]
print(arr)

