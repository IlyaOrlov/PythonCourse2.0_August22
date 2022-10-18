# изучение документации к библиотеке itertools

# chain.from_iterable - выполняет объединение списков

# filterfalse - Для создания нового списка из уже имеющейся последовательности объектов

# combinations - Первая функция по комбинированию отдельных элементов последовательности принимает
# два аргумента, как и все последующие. Первый позволяет задать определенный объект,
# а второй – количество значений, которые будут присутствовать в каждом новом отрезке


import itertools

lst = ([1, 2, 3], [4, 5], [6, 7])
s = list(itertools.chain.from_iterable(lst))
print(s)

lst1 = (['hello', 'i', 'write', 'cool', 'code'])
b = list(itertools.filterfalse(lambda i: len(i) < 5, lst1))
print(b)

c = list(itertools.combinations('password', 4))
print(c)

