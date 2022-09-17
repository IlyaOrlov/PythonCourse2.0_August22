def dec(fun):


    def dec_in():
        b = '==========='
        c = '==========='
        print(b)
        fun()
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

@dec
def fun_input():
    print(a)


while True:
    a = input('Введите число: ')
    fun_input()
    if fun_return():
        continue
    else:
        break

