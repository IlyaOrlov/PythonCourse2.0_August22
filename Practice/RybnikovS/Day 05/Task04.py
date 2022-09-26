import random


def matrix_make():
    inner_arr = []
    input_size = input("Введите размерность матрицы n*k через пробел: ")
    numbers = [int(i) for i in input_size.split(" ")][:2]
    for row in range(numbers[0]):
        inner_arr.append([0] * numbers[1])
    for row in range(numbers[0]):
        for column in range(numbers[1]):
            inner_arr[row][column] = random.randint(1, 50)
    return inner_arr


def array_print(inner_arr, comment: str):
    print(comment)
    for row in range(len(inner_arr)):
        for column in range(len(inner_arr[row])):
            print(inner_arr[row][column], end='  ')
        print()


def matrix_delete_column(inner_arr, column):
    for row in inner_arr:
        row.pop(column)
    return inner_arr


def find_column_for_del(inner_arr, inner_elem):
    new_array = []
    for row in range(len(inner_arr)):
        for column in range(len(inner_arr[row])) :
            if inner_arr[row][column] == inner_elem:
                new_array.append(column)
    return new_array


# my_array = matrix_make()
my_array = [[1, 2, 3],
            [4, 5, 2],
            [6, 7, 8]]  # матрица для отладки

array_print(my_array, "Текущая матрица")

elem_for_del = int(input("Введите элемент для удаления столбца: "))
num_column_for_del = find_column_for_del(my_array, elem_for_del)

for elem in reversed(num_column_for_del):
    matrix_delete_column(my_array, elem)

array_print(my_array, "Новая матрица")
