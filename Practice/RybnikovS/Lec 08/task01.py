class MyIterator:

    def __init__(self, file_name, parameter):
        self._parameter = parameter
        self._f = open(file_name, encoding="utf")

    def __iter__(self):
        return self

    def __next__(self):
        temp = " "
        res = ""
        if temp != "":
            while temp != "":
                temp = self._f.read(1)
                if temp == self._parameter:
                    break
                else:
                    res += temp
            return res
        else:
            raise StopIteration

    def __del__(self):
        self._f.close()


it_text = MyIterator("task01_text.txt", "§")
print(next(it_text))
print(next(it_text))
print(next(it_text))
print(next(it_text))
