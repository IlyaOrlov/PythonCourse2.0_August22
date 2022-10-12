# Реализовать итератор, который бы "читал" заданный текст по параграфам.
# Символ параграфа задается отдельно.


class MyIterator:
    def __init__(self, file, sym):
        self.file = file
        self.sym = sym

    def __iter__(self):
        return self

    def __next__(self):
        my_str = ' '
        res = ""
        while my_str != "":
            my_str = self.file.read(1)
            if my_str == self.sym:
                break
            else:
                res += my_str
        if my_str != "":
            return res
        else:
            raise StopIteration


with open("my_file.txt", "r") as f:
    for i in MyIterator(f, "&"):
        print(i)
