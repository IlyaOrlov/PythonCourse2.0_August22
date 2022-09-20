def dec_0(fun):
    def dec_in(*args, **kwargs):
        b = '==========='
        c = '==========='
        print(b)
        res = fun(*args, **kwargs)
        print(c)
        return res
    return dec_in

def dec_1(fun):
    def dec_in(*args, **kwargs):
        b = '+++++++++++'
        c = '+++++++++++'
        print(b)
        res = fun(*args, **kwargs)    # fun(*args, **kwargs)
        print(c)
        return res    # а эту строку удалить
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
def fun_input(*args):
    print(*args)


while True:
    a, x, y = input('Введите число: '), input('Введите число: '), input('Введите число: ')
    fun_input(a, x, y)
    if fun_return():
        continue
    else:
        break
