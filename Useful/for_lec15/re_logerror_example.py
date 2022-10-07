import re


result = []
with open('logfile.txt') as f:
    pattern = re.compile(r'ERROR-.*')
    for line in f:
        res = re.findall(pattern, line)
        result += res

print(result)
