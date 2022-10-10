def decorator_my(fun):
    def inner_fun(*args, **kwargs): # args = (10, 20)  kwargs = {p: 10}
        print(f'{args=}, {kwargs=}') # (10, 20), {p: 10}
       # print(*args, **kwargs) # 10, 20, p=10  Error
        res = fun(*args, **kwargs)
        print('===========')
        return res

    return inner_fun


@decorator_my
def myfun(x, y):
    return x + y


#myfun = decorator_my(myfun )
p = 2 * myfun(10, 20)
print(f'периметp равен: {p}')
print('========')
