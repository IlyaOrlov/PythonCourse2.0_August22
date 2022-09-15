str_num = ""

while True:
    s = input('Введите число: ')

    if s.lower() == 'stop':
        break

    if not s.isdecimal():
        print('--Введите только число--')
        continue

    str_num += s
    print(str_num)
