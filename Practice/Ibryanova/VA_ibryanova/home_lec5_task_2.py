def fun(num):
    for i in range(len(num)):
       if num[i] in lst1:
           print({num[i]})
           break
       else:
           lst1.add(num[i])

lst = [2, 3, 4, 5, 3, 2]
lst1 = set()
fun(lst)



