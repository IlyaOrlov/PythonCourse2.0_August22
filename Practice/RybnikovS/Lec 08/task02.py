def iter_file_by_line(filename):
    with open(filename, encoding="utf") as f:
        for line in f:
            yield line


x = iter_file_by_line("task01_text.txt")
for i in x:
    print(i)

