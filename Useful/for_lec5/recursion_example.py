import sys


def fact(x):
    if x < 3:
        return x
    return x * fact(x - 1)


res = fact(5)
print(res)


# 2! = 2
# 3! = 3 * 2!
# 4! = 4 * 3!
# 5! = 5 * 4!

