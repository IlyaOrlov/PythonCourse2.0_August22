import os
import shutil
from datetime import datetime as dt


file_path = input("Введите путь к файлу: ") or "./test"
while True:
    lst_dir = list(os.walk(file_path))
    now = dt.timestamp(dt.now())
    if len(lst_dir) > 1:
        for d in lst_dir:
            main_folder = d[0]
            folders = d[1]
            files = d[2]
            res_dir = now - os.path.getctime(main_folder)
            if res_dir > 120 and files == [] and folders == []:
                print(f"del {main_folder}")
                shutil.rmtree(main_folder)
                break
            else:
                if files:
                    for f in files:
                        res_file = now - os.path.getctime(f"{main_folder}/{f}")
                        if res_file > 60:
                            print(f"del {f}")
                            os.remove(f"{main_folder}/{f}")
    else:
        print("Все файлы удалены")
