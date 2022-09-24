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


def matrix_delete_column(inner_arr):
    column_for_del = int(input("Введите столбец для удаления: "))
    for row in inner_arr:
        row.pop(column_for_del)
    return inner_arr


my_array = matrix_make()
array_print(my_array, "Текущая матрица")
my_array = matrix_delete_column(my_array)
array_print(my_array, "Новая матрица")

