import os
import shutil
from datetime import datetime as dt


file_path = input("Введите путь к файлу: ") or "./test"
while True:
    lst_dir = list(os.walk(file_path))
    now = dt.timestamp(dt.now())
    if len(lst_dir) > 1:
        for d in lst_dir:
            res_dir = now - os.path.getctime(d[0])
            if res_dir > 120:
                print(f"del {d[0]}")
                shutil.rmtree(d[0])
                break
            else:
                d2 = d[2]
                if d2:
                    for f in d2:
                        res_file = now - os.path.getctime(f"{d[0]}/{f}")
                        if res_file > 60:
                            print(f"del {f}")
                            os.remove(f"{d[0]}/{f}")
    else:
        print("Все файлы удалены")
