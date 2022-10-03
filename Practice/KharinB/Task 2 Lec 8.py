def read_gen(file_path):
    with open(file_path, 'r') as f:
        res = f.read(1)
        while res:
            s = f.read(1)
            if s == "\n" or s == "":
                yield res
                res = f.read(1)
            else:
                res += s

for i in read_gen("text.txt"):
    print(i)