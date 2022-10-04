class MyIterator:

    def __init__(self, f, parameter):
        self._f = f
        self._parameter = parameter

    def __iter__(self):
        return self

    def __next__(self):
        temp = " "
        res = ""
        while temp != "":
            temp = self._f.read(1)
            if temp == self._parameter:
                break
            else:
                res += temp
        if res[-1] == "\n":
            res = res[:-1]
        return res


with open("task01_text.txt", encoding="utf") as f:
    it_text = MyIterator(f, "§")
    print(next(it_text))
    print(next(it_text))
    print(next(it_text))
    print(next(it_text))
