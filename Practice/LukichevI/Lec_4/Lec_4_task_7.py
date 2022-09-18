def dec_0(fun):
    def dec_in(*args, **kwargs):
        b = '==========='
        c = '==========='
        print(b)
        fun(*args, **kwargs)
        print(c)
    return dec_in

def dec_1(fun):
    def dec_in(*args, **kwargs):
        b = '+++++++++++'
        c = '+++++++++++'
        print(b)
        fun(*args, **kwargs)
        print(c)
    return dec_in


def fun_return():
    d = (input('Хотите продолжить? да/нет: '))
    d = d.lower()
    if d == 'да':
        return True
    else:
        print('Как скажете.')
        return False
@dec_0
@dec_1
def fun_input(*args, **kwargs):
    print(a, x, y)


while True:
    a, x, y = input('Введите число: '), input('Введите число: '), input('Введите число: '),
    fun_input()
    if fun_return():
        continue
    else:
        break

