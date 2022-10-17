#lst = [2, 3, 4, 5, 'hello', 2]
##el = lst[0]
##el = lst[1]
##str(el1) > str(el)
#res = lst.sort(key=lambda el: str(el))
#print(res)
#print(lst)


#def fun(x, arg):
#   x += 100 # x = 1000 + 100
#    arg.append(100) #  если arg = 100, то принт будет [1, 2, 3]

#n = 1000
#lst = [1, 2, 3]
#fun(n, lst)
#print(n) # 1000
#print(lst) #  [1, 2, 3, 100]



#lst1 = [1, 2, 3]
#lst2 = lst1.copy() # этот метод позволяет создать новый список, который не будет влиять на оригинал
#lst2.append(100)
#print(lst1)
#print(lst2)

import copy


lst1 = [1, 2, 3, [500]]
lst2 = copy.deepcopy(lst1) #глубокое копирование
lst2[3].append(100)
print(lst1)
print(lst2)
