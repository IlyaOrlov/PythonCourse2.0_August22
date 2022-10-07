import re

pattern = re.compile(r"git [a-z]{3,8} (?:(?:|--set-upstream\s)origin .*|.*.py|"
                     r"(?:https|.*@)[a-zA-Z0-9_/./:]*\.git"
                     r"|-\w (?:\w+|\".*\"))")
'(git [^а-я"\n)]+("[а-яА-Я ]+")?)'

with open(r"../../README.md", encoding="utf") as file:
    f = file.read()
print(f)
x = re.findall(pattern, f)
print(x)
