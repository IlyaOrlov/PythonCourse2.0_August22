FILENAME = '1.txt.txt'
t = ('hello', 'bye', 'good luck')

f = open(FILENAME, 'w+')
for i in t:
    line = f'{i}\n'
    f.write(line)
    cur_pos = f.tell()
    f.seek(cur_pos - len(line) - 1)
    res = f.read()
    print(res)
f.close()