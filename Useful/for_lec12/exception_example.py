class MyException(Exception):
    pass

class MyClass:
    def __init__(self, x):
        if type(x) is int:
            self.attr = 10 / x
        else:
            raise MyException("Ну нельзя же такое вводить!")

def fun(y):
    ex = MyClass(y)
    print("Hello")

def fun1(z):
    try:
        fun(z)
    except ZeroDivisionError:
        print("Произошла ошибка деления на ноль. Ничего страшного. Идём дальше")
    except Exception as x:
        print(f"Произошла какая-то ошибка: {x}. Ничего страшного. Идём дальше")
    print("Без паники!")


m = input("Input number: ")
fun1(m)
