def fun(num):
    s = set()
    for i in range(len(num)):
       if num[i] in s:
           print(num[i])
           break
       else:
           s.add(num[i])

lst = [2, 3, 4, 5, 3, 2]
fun(lst)



