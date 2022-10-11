# -*- coding: utf-8 -*-
def read_line(file):
    try:
        with open(file, "r") as f:
            for stroka in f:
                yield stroka
    except:
        print("Ошибка при чтении файла")



for i in read_line("text4.txt"):
    print(i)
    print("=======")