def fun(a):
    return a * a


def mygen(n):
    cur = 0
    step = 2
    count = 0
    while count < n:
        yield cur
        cur += step
        count += 1


res = mygen(10)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
