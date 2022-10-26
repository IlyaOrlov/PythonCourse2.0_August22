#Написать программу, которая уничтожает файлы и папки по истечении заданного времени.
# Вы указываете при запуске программы путь до папки, за которой нашему скрипту необходимо следить.
# После запуска программа не должна прекращать работать, пока вы не остановите ее работу с помощью Ctrl+C
# (подсказка: для постоянной работы программы необходим вечный цикл, например, "while True:",
# при нажатии Ctrl+C автоматически остановится любая программа).
# Программа следит за объектами внутри указанной при запуске папки и удаляет их тогда,
# когда время их существования становится больше одной минуты для файлов и больше двух минуты для папок
# (то есть дата создания отличается от текущего момента времени больше чем на одну/две минуты).
# Ваш скрипт должен смотреть вглубь указанной папки. Например, если пользователь создаст внутри нее папку,
# внутри нее еще одну, а внутри этой какой-то файл, то этот файл должен удалиться первым
# (так как файлу положено жить только одну минуту, а папкам две). Вам понадобятся библиотеки os и shutil
import os
import datetime
import shutil


def delete_file_or_dir(path):
    while True:
        for i, dirs, files in os.walk(path):
            for f in files:
                path_to_file = os.path.join(i, f)
                del_time =\
                    datetime.datetime.now()\
                    - datetime.datetime.fromtimestamp(os.path.getctime(path_to_file))
                if del_time > datetime.timedelta(seconds=60):
                    os.remove(path_to_file)

            for d in dirs:
                path_to_dir = os.path.join(i, d)
                del_time =\
                    datetime.datetime.now()\
                    - datetime.datetime.fromtimestamp(os.path.getctime(path_to_dir))
                if del_time > datetime.timedelta(seconds=120):
                    shutil.rmtree(path_to_dir)


delete_file_or_dir('/Users/user/Desktop/Новая папка (2)')