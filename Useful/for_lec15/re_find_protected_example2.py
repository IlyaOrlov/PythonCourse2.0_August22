import re


lst = ["_a", "b", "__c", "d", "_e"]
s = re.compile("_[^_].*")
for i in lst:
    if re.match(s, i):
        print(i)
