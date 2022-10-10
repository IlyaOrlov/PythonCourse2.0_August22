d = {'dog': 'собака', 'table': 'стол', 'four': 'четыре'}
#d['dog'] = 'пес'# можно изменить
#d['cat'] = 'кот'# можно добавить
print(d.get('abc', ''))# get позволяет, если элемент отсут-т в словаре - выдать none вместо ошибки

for i in d:
    print(i)


d2 = {v: k for k, v in d.items()}
print(d2)

#если мы хотим отследить что ввел пользователь то(расчет статистики):
d = dict()
while True:
    i = input('Input something: ')
    if i == 'stop':
        break
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
