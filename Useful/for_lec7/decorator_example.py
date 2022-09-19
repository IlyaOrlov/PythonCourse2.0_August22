def decorator(fun):
    def inner_fun(*args, **kwargs):  # args = (10, 20), kwargs = {p: 10}
        print(f"{args=}, {kwargs=}")  # (10, 20), {p: 10}
        # print(*args, **kwargs)  # 10, 20, p=10  # Error!
        res = fun(*args, **kwargs)  # 10, 20, p=10
        print("end of function")
        return res

    return inner_fun

@decorator
def myfun(x, y, z):
    return x + y + z

#myfun = decorator(myfun)
p = 2 * myfun(10, 20)
print(f"Периметр: {p}")
