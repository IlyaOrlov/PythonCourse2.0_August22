def rep(arr):
    for i in range(len(arr)):
        if arr[i] in arr[:i:]:
            return arr[i]

arr = [2, 3, 7, 5, 3, 2]
res = rep(arr)
print(res)