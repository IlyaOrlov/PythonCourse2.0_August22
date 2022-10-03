#import work_lec4_function


#s = input("Введите строку с цифрами: ")
#work_lec4_function.myfun(s)

def fun(a, b=5):
    print(f"{a=}")
    print(f"{b=}")


fun(10, 20)
fun(12)
fun(14)