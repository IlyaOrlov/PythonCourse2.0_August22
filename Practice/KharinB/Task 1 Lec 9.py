import re

with open("../README.md", encoding="utf") as f:
    for st in f:
        a = re.findall(r"git [\w]+ ?[!-~]* *[A-z]+ *[\"]{1}[\D]+[\"]{1}", st) \
            or re.findall(r"git [\w]+ ?[!-~]* *[A-z]+", st)
        if a:
            print(a)
# Первое выражение выводит только: git commit -m "Любой разумный комментарий к сделанным изменениям",
# второе выражение (после or) выводит все остальные
