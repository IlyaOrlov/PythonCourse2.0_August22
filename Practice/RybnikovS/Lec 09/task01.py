import re

pattern = r"git \w+ [-]\w+"
with open(r"../../README.md", encoding="utf") as file:
    f = file.read()
print(f)
x = re.findall(pattern, f)
print(x)
