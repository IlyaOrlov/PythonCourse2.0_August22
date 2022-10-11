class MyIterator:

    def __init__(self, file_name, parameter):
        self._parameter = parameter
        self._f = open(file_name, encoding="utf")
        self.temp = " "

    def __iter__(self):
        return self

    def __next__(self):
        res = ""
        if self.temp != "":
            while True:
                self.temp = self._f.read(1)
                if self.temp != self._parameter:
                    res += self.temp
                    if self.temp == "":
                        return res
                else:
                    return res
        else:
            raise StopIteration

    def __del__(self):
        self._f.close()


it_text = MyIterator("task01_text.txt", "§")
for i in it_text:
    print(i)
