import copy


lst1 = [1, 2, 3, [500]]
lst2 = copy.deepcopy(lst1)
lst2[3].append(100)
print(lst1)
print(lst2)
