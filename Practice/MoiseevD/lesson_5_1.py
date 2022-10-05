def current_index(arr, idx):
    idx_min = idx
    i = idx
    # while i < len(arr):
    #     if arr[i] < arr[idx_min]:
    #         idx_min = i
    #     i += 1
    for i in range(idx, len(arr)):
        if arr[i] < arr[idx_min]:
            idx_min = i
        i += 1
    return idx_min


def min_element(elm):
    for i in range(len(elm)):
        cur_idx = current_index(elm, i)
        if cur_idx != i:
            elm[cur_idx], elm[i] = elm[i], elm[cur_idx]
    return elm


a = [0, 3, 24, 2, 3, 7]
res = min_element(a)
print(res)
