string_of_marks = 'Оценки по экзамену: Петров - 3, Сидоров - 4, Иванов - 2, Круглов - болел, Максимов - 5'
dict_of_marks = {"болел": 'Неявка', 5: 'Отлично', 4: 'Хорошо', 3: 'Удовлетворительно', 2: 'Не удовлетворительно'}

print(f'До \n{string_of_marks}')
for key in dict_of_marks:
    string_of_marks = string_of_marks.replace(str(key), str(dict_of_marks[key]))
print(f'После \n{string_of_marks}')