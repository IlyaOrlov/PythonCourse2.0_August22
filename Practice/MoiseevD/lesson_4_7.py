def decor_start(start):
    def decor_finish(*args, **kwargs):
        print("=====1======")
        res = start(*args, **kwargs)
        print("=====2======")
        return res
    return decor_finish


@decor_start
def start_finish(start):
    print(start)


start_finish('=================')

