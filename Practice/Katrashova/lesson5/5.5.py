with open("text.txt", "r") as fo:
    reading = fo.read()
my_choice = input("Что заменить? 1 - табуляция на пробелы, 2 - пробелы на табуляцию \n")

with open("text.txt", "w") as fw:
    if my_choice == "1":
        fw.write(reading.replace("\t", "    "))
    elif my_choice == "2":
        fw.write(reading.replace("    ", "\t"))
print("Файл изменен")