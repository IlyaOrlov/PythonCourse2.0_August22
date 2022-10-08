def my_decor(func):
    def wrapper():
        print("===========")
        func()
        print("===========")
    return wrapper

def my_func():
    print("Тут основная функция")
my = my_decor(my_func)
my()