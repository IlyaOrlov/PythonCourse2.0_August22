def decorator(fun):
    def in_decorator(*args, **kwargs):
        print("===========")
        res = fun(*args, **kwargs)
        print("===========")
        return res

    return in_decorator


@decorator
def my_example(x):
    return x * x

res = my_example(10) * 2
print(res)



#
# # 1й способ
# @decorator
# def max_number(a, b):
#     if a > b:
#         print(a)
#     else:
#         print(b)
#
# def max_number2(a, b):
#     if a > b:
#         print(a)
#     else:
#         print(b)
#
# x = input("Введите 'a': ")
# y = input("Введите 'b': ")
# max_number(x, y)
#
# # 2й способ
# max_number2 = decorator(max_number2)
#
# n = input("Введите 'a': ")
# m = input("Введите 'b': ")
# max_number2(n, m)