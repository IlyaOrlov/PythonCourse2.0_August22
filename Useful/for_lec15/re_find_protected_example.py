import re


d = ['_name', '_surname', 'salary', '__secret']
# Нужно распечатать все protected атрибуты

pattern = '^_[^_].*'
for i in d:
    res = re.findall(pattern, i)
    if res:
        print(res)
