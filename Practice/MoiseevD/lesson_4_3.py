str_num = ""

while True:
    s = input('Введите число, для выхода введите "stop" : ')

    if s.lower() == 'stop':
        break

    if not s.isdecimal():
        print('--Введите только число--')
        continue

    str_num += s
print(str_num)
