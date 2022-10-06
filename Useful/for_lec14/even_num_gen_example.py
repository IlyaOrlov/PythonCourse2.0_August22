def gen_fun(limit):
    i = 0
    step = 2
    while i < limit:
        yield i
        i += step
        

for x in gen_fun(10):
    print(x)



