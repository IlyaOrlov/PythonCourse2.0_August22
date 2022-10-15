import os
import datetime
import shutil


def modification_date(filename):
    t = os.path.getctime(filename)
    return (datetime.datetime.now() - datetime.datetime.fromtimestamp(t)).seconds


def show_dir(cur_path):
    global dict_files
    global dict_folders
    for i in os.listdir(cur_path):
        path = os.path.join(cur_path, i)
        if os.path.isfile(path):
            dict_files[path] = modification_date(path)
        else:
            dict_folders[path] = modification_date(path)
            show_dir(path)


dict_files = {}
dict_folders = {}
file_time = 60
folder_time = 120
path_for_delete = "12312"
while True:
    show_dir(path_for_delete)
    if not dict_folders and not dict_files:
        print(f"Больше нечего удалять")
        break
    else:
        for i in dict_files.keys():
            if dict_files[i] == file_time:
                print(f"Удален файл {i}")
                os.remove(i)
                del dict_files[i]
                break
        for i in dict_folders.keys():
            if dict_folders[i] == folder_time:
                print(f"Удалена папка {i}")
                shutil.rmtree(i)
                del dict_folders[i]
                break




