#-*- coding: utf-8 -*-
import re

st = re.compile(r"git [a-z]{3,4} \Z|git [a-z]{4,8} \W+[a-z]{1,3}\W+[a-z]{2,8}.[a-z]{6}|git [a-z]{4,8}.{55}|git [a-z]{3,4} [a-z]{6}.?[a-z]{2,4}|git [a-z]{3,4}")
with open(r"../README.md", encoding="utf") as f:
    txt = f.read()

res1 = re.findall(st, txt)
print(res1)








#git clone https://github.com/IlyaOrlov/PythonCourse2.0_August22.git "git [a-z]{4,8}\W{55}git
#git checkout -b my_branch "git [a-z]{4,8} \W+[a-z]{1,3}\W+[a-z]{2,8}.[a-z]{6}"
#git push --set-upstream origin my_branch git [a-z]{4,8} \W+[a-z]{1,3}\W+[a-z]{2,8}.[a-z]{6} my_branch"
#git commit -m "Любой разумный комментарий к сделанным изменениям" r"git [a-z]{4,8} \W+[a-z]{1,3}\W"
#git@github.com:IlyaOrlov/PythonCourse2.0_August22.git r"git.?[a-z]{6}.[a-z]{3}.{39}"
#git push    r"git [a-z]{3,4}
#git add
#git add mytest.py    r"git [a-z]{3,4} [a-z]{6}.?[a-z]{2,4}
#git pull origin main r"git