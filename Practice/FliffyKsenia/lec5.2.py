i=0
arr = [2, 3, 4, 5, 3, 2]
for i in range (0, len(arr) -1):
    if arr.index(arr[i]) < i:
        print(arr[i])
