name = input('Введите имя: ')


def decorator_function(func):
    def wrapper():
        print('===========')
        func()
        print('===========')

    return wrapper


@decorator_function
def welcome():
    print(f'Добро пожаловать, {name}')

welcome()