class Fun:
    def __init__(self):
        print('init called')

    def __call__(self, *args, **kwargs):
        print('call called')
        return sum(args)


f = Fun()  # Функтор == функциональный объект
print(f(1, 2))
print(f(100, 200))