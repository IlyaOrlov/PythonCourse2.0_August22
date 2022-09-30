#вариант №1
def decorator(myfun):
    def wrapper(*args, **kwargs):
        print("==============")
        res = myfun(*args, **kwargs)
        print("==============")
        return res

    return wrapper


def mysum(a, b, c, d):
    return a+b+c+d


mysum=decorator(mysum)
print(mysum(300, 700, 900, 1300))

#вариант №2
@decorator
def mymul(a, b, c, d):
    return a*b*c*d


print(mymul(300, 700, 900, 1300))