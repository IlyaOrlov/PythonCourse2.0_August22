def myfun(x):
    s1 = ""
    for i in x:
        if i.isdecimal():
            s1 += "*"
        else:
            s1 += i
    return s1


s = "asdg1dfg4dg6"
res1 = myfun(s)
print(res1)

s2 = "12354fdg689"
res2 = myfun(s2)
res2 = res2.replace("*", " ")
print(res2)