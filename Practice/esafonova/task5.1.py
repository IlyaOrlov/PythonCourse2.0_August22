def sort(arr):
    for i in range(len(arr)):
        m = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[m]:
                m = j
        if m != i:
            arr[m], arr[i] = arr[i], arr[m]
    return arr


res = sort(arr)
print(res)