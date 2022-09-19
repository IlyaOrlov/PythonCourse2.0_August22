def sort(arr):
    for i in range(len(arr)):
        m = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[m]:
                m = j
        arr[m], arr[i] = arr[i], arr[m]
    return arr

arr = [6,3,24,2,3,7]
res = sort(arr)
print(res)