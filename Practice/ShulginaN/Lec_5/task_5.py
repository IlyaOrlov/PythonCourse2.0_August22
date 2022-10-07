# Реализовать функциональность, которая бы “сворачивала” и “разворачивала” символы табуляции в файле.
# То есть, на вход передается файл, необходимо заменить все символы табуляции на четыре пробела,
# либо же заменить все комбинации из четырех символов пробела на символ табуляции
# (в зависимости от опции указанной пользователем).


with open("my_file.txt", "r") as fo:
    reading = fo.read()
my_choice = input("Что необходимо заменить? 1 - табуляция на пробелы, 2 - пробелы на табуляцию \n")

with open("my_file.txt", "w") as fw:
    if my_choice == "1":
        fw.write(reading.replace("\t", "    "))
    elif my_choice == "2":
        fw.write(reading.replace("    ", "\t"))
print("Заменил,см. my_file")

