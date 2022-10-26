#Используя модуль re, найти все команды Git с аргументами в файле Practice/README.md
# git clone https://github.com/IlyaOrlov/PythonCourse2.0_August22.git
# git clone git@github.com:IlyaOrlov/PythonCourse2.0_August22.git
# git checkout -b my_branch
# git push --set-upstream origin my_branch
# git add
# git add mytest.py)
# git commit -m "Любой разумный комментарий к сделанным изменениям"
# git pull origin main
# git push
import re

with open("../README.md", encoding="utf-8") as f:
    for i in f:
        # pattern = r'git [a-z]+[ ]+[a-z]+.{3}[a-z]+\W\w*\W\w*\W\w*\d\W\d.{1}\w*.{1}\w*'
        pattern = r'git [\a-z]+ ?[!-~]* *[a-z]+'
        search_git = re.findall(pattern, i)
        if search_git != []:
            print(search_git)

with open("../README.md", encoding="utf-8") as f1:
    for i in f1:
        pattern_next = r'git [\a-z]+ ?[!-~]* *[A-z]+ *[\"]{1}[\D]+[\"]'
        search_git_next = re.findall(pattern_next, i)
        if search_git_next != []:
            print(search_git_next)