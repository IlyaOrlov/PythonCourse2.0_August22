import os
import time
# просим у пользователя имя папки в которой нужна чистота.
source = input("Введите имя папки за чистотой которой надо следить: ")

# функция рекурсивного удаления каталогов.
def remove_dir(dir_path):
    # строим древо каталогов от пути переданного в функцию
    for oswalk in  os.walk(dir_path):
        # удаляем все файлы в директории
        for files in oswalk[2]:
            file_path = os.path.join(oswalk[0],files)
            if os.path.isfile(file_path):
                os.remove(file_path)
        # если каталог пуст, удаляем иначе идем в рекурсию.
        if oswalk[1]+oswalk[2]==[]:
            os.rmdir(dir_path)
        else:
            for dirs in oswalk[1]:
                remove_dir(os.path.join(oswalk[0],dirs))


while True:
    # раз в секунду смотрим в нутри требуемой папки на предмет устаревших файлов и папок
    time.sleep(1)
    # строим древо каталогов
    for oswalk in os.walk(source):
        path = oswalk[0]
        # обходим все папки
        for dirs in oswalk[1]:
            # строим путь до конкретной папки
            path = os.path.join(oswalk[0], dirs)
            # заправиваем время создания папки
            create_time = os.path.getctime(path)
            # проверяем, если папка создана больше чем 120 секунд назад вызываем функцию удаления папки.
            if create_time+120<time.time() and source!=path:
                remove_dir(path)
        # обходим все файлы
        for files in oswalk[2]:
            # строим путь до конкретного файла.
            path = os.path.join(oswalk[0], files)
            # запрашиваем время создания файла
            create_time = os.path.getctime(path)
            # если время создания файла больше, чем 60 секунд назад удаляем файл.
            if create_time + 60 < time.time():
                print(path)
                os.remove(path)
