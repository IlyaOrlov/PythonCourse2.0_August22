# Написать программу, которая уничтожает файлы и папки по истечении заданного времени.
# Вы указываете при запуске программы путь до папки, за которой нашему скрипту необходимо следить.
# После запуска программа не должна прекращать работать, пока вы не остановите ее работу с помощью Ctrl+C
# (подсказка: для постоянной работы программы необходим вечный цикл, например, "while True:", при нажатии
# Ctrl+C автоматически остановится любая программа). Программа следит за объектами внутри указанной при
# запуске папки и удаляет их тогда, когда время их существования становится больше одной минуты для файлов
# и больше двух минуты для папок (то есть дата создания отличается от текущего момента времени больше чем на
# одну/две минуты). Ваш скрипт должен смотреть вглубь указанной папки. Например, если пользователь создаст
# внутри нее папку, внутри нее еще одну, а внутри этой какой-то файл, то этот файл должен удалиться первым
# (так как файлу положено жить только одну минуту, а папкам две).
# Вам понадобятся библиотеки os и shutil.
import os
import shutil
from datetime import datetime as dt


file_path = input("Введите путь к папке с файлами для удаления данных: ")
while True:
    lst_dir = list(os.walk(file_path))
    now = dt.timestamp(dt.now())
    if len(lst_dir) > 1:
        for i in lst_dir:
            res = now - os.path.getctime(i[0])
            if res > 120 and i[2] == [] and i[1] == []:
                shutil.rmtree(i[0])
                break
            else:
                d2 = i[2]
                if d2:
                    for f in d2:
                        res = now - os.path.getctime(f"{i[0]}/{f}")
                        if res > 60:
                            os.remove(f"{i[0]}/{f}")
        else:
            print("Готово")
