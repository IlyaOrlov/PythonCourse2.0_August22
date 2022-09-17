arr = [0, 3, 0, 24, 2, 3, 8, 6, 8, 78, 8, 7]
for i in range(len(arr)):
    if arr[i] >= arr[arr[i::].index(min(arr[i::])) + i]:
        arr[arr[i::].index(min(arr[i::])) + i], arr[i] = arr[i], arr[arr[i::].index(min(arr[i::])) + i]
print(arr)
