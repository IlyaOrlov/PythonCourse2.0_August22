def decor_start(start):
    def decor_finish(*args, **kwargs):
        res = start(*args, **kwargs)
        return res
    return decor_finish


@decor_start
def start_finish(start):
    print(f'После запуска функции {start}')

line = "============"
print(f'До запуска функции {line}')
start_finish(line)
