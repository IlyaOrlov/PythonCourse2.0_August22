def sort(arr):
    for i in range(len(arr)):
        num = i

        for a in range(i + 1, len(arr)):
            if arr[a] < arr[num]:
                num = a
        if num != i:
            arr[num], arr[i] = arr[i], arr[num]

    return arr

arr = [0,3,24,2,3,7]
print(sort(arr))