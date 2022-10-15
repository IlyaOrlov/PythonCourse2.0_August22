import re


with open("README.txt", "r") as f:
    pattern = re.compile(r"git [a-z]+")
    for line in f:
        res = re.findall(pattern, line)
        print(res)