def prov():  # Функция для проверки ввода.
    while True:
        i = input("Введите число: ")
        if i.isdecimal():
            i = int(i)
            return i
        else:
            print("Введено не число.")


def return_answer():  # Функция возвращает большее число.
    x = prov()
    y = prov()
    return x if x > y else y


def print_answer():  # Функция печатает большее число.
    x = prov()
    y = prov()
    print(x if x > y else y)


а = return_answer()
print(а)  # Проверка возвращённого значения

print_answer()
