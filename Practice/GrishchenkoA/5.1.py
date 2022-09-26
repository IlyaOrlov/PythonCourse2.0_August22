def find_min_index(lst):
    for i,d in enumerate(lst):
        d = min(lst[i:])
        d, lst[i] = lst[i], d


arr = [0, 3, 24, 2, 3, 7]
#for i in range(0, len(arr)):
find_min_index(arr)
print(arr)

#def find_min_index(lst):
  #  a = min(lst[i:])
   # c = lst.index(a, i)
    #lst[c], lst[i] = lst[i], lst[c]


#arr = [0, 3, 24, 2, 3, 7]
#for i in range(0, len(arr)):
   # find_min_index(arr)
#print(arr)