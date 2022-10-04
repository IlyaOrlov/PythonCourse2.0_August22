# 7.Написать декоратор, выводящий "===========" до и после запуска функции.


def mysum(x, y):
    return x + y


def mymul(x, y):
    return x * y


def decorator_fun(func):
    def wrapper(*args, **kwargs):
        print("===========")
        res = func(*args, **kwargs)
        print(res)
        print("===========")
        return res
    return wrapper


mysum = decorator_fun(mysum)
mymul = decorator_fun(mymul)

mysum(10, 20)
mymul(10, 20)

# 1.Реализовать алгоритм сортировки выбором. Алгоритм состоит из следующих шагов:
# 1.найти наименьший элемент в массиве
# 2.поменять местами его и первый элемент в массиве
# 3.найти следующий наименьший элемент в массиве
# 4.и поменять местами его и второй элемент массива
# 5.продолжать это пока весь массив не будет отсортирован
# arr = [0,3,24,2,3,7]
#
# // здесь реализованный алгоритм
#
# // на выходе должен получиться список, содержащий [0, 2, 3, 3, 7, 24]

# arr = [0,3,24,2,3,7]
# newarr = []
# while len(arr) > 0:
#     newarr.append(min(arr))
#     arr.remove(min(arr))
# print(newarr)

def sort(arr):
    for i in range(len(arr)):
        m = i # индекс элемента
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[m]:
                m = j
        if m != i:
            arr[m], arr[i] = arr[i], arr[m]
    return arr


arr = [4,3,24,2,3,7]
res = sort(arr)
print(res)


# 2.Написать и вызвать функцию, возвращающую первый повторившийся символ в переданном списке.
# Например, для  списка [2, 3, 4, 5, 3, 2] функция должна вернуть 3.


def retrep(arr):
    for i in arr:
        if arr[i] in arr[:i:]:
            return arr[i]


arr = [2, 3, 4, 5, 3, 2]
res = retrep(arr)
print(res)

# 3.Найти и заменить некие шаблоны в строке: есть строка с определенного вида форматированием,
# необходимо заменить в этой строке все вхождения шаблонов на их значение из словаря.

d = {"туда":"в даль", "ведет":"идет", "длинная":"продолжительная","тропа":"дорога"}
s = "туда ведет длинная тропа..."

print(f'Первоначальная строка: \n{s}')
for key in d:
    s = s.replace(str(key), str(d[key]))
print(f'Изменённая строка: \n{s}')

# 4.Есть список списков (матрица). Каждый внутренний список – это строка матрицы.
# Необходимо реализовать функцию, которая удаляет столбец, который содержит заданную цифру.


def delcolumn(anylist, num):
    for row in anylist:
        for i in reversed(range(len(row))):
            if row[i] == num:
                [row.pop(i) for row in anylist]
    print(anylist)



mylist = [[1, 2, 3], [4, 5, 1], [1, 6, 7]]
delcolumn(mylist, 1)

# 5.Реализовать функциональность, которая бы “сворачивала” и “разворачивала” символы табуляции в файле.
# То есть, на вход передается файл, необходимо заменить все символы табуляции на четыре пробела,
# либо же заменить все комбинации из четырех символов пробела на символ табуляции (в зависимости от опции,
# указанной пользователем).

def tab(filename):
    with open(filename) as fileobject:
        lines = fileobject.readlines()
    mystring = ''
    for line in lines:
        mystring += line.replace('  ', '    ')
        # mystring.replace('\t', '    ')
    print(mystring)

def wspace(filename):
    with open(filename) as fileobject:
        lines = fileobject.readlines()
    mystring = ''
    for line in lines:
        mystring += line.replace('    ', '  ')
        # mystring.replace('\t', '    ')
    print(mystring)

# tab('hw6.txt')
user_option = input("Пожалуйста введите номер опции(1 - заменить табуляцию на пробелы, 2 - заменить пробелы на табуляцию): ")
if user_option == "1":
    tab('hw6.txt')
elif user_option == "2":
    wspace('hw6.txt')
else:
    print(f"Вы ввели не допустимое значение.")







