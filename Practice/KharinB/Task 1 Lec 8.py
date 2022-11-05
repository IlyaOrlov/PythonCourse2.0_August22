class MyIterTxt:

    def __init__(self, f, sim):
        self._file_path = f
        self._sim = sim
        self._ind = 0

    def __iter__(self):
        return self

    def __next__(self):
        with open(self._file_path, "r") as f:
            f.seek(self._ind)
            s = f.read(1)
            res = ""
            if s != "":
                while True:
                    s = f.read(1)
                    if s != self._sim and s != "":
                        res += s

                    else:
                        self._ind = f.tell()
                        return res

            else:
                raise StopIteration


for i in MyIterTxt("text.txt", "@"):
    print("________________")
    print(i)
