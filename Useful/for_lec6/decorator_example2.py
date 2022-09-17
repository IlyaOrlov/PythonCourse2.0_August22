import time


def time_checker(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        r = f(*args, **kwargs)
        stop = time.time()
        print(f"Time spent: {stop - start}")
        return r

    return wrapper


def hello_bye(original_fun):
    def inner(*args, **kwargs):
        # ваш код для выполнения до вызова функции
        res = original_fun(*args, **kwargs)
        # ваш код для выполнения после вызова функции
        return res

    return inner



def fun(a, b, c):
    return a + b + c


if __name__ == "__main__":
    fun = time_checker(hello_bye(fun))
    fun(100, 500, 1000)