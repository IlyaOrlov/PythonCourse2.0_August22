import re


with open("README.md", "r") as f:
    pattern = re.compile(r"git [a-z]+\w\b")
    for line in f:
        res = re.findall(pattern, line)
        print(res)