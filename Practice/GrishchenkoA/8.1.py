
class IterRead:
    def __init__(self, file_new, symbol):
        self.file_new = file_new
        self.symbol = symbol
        self.ind = 0


    def __iter__(self):
        return self

    def __next__(self):
        try:
            with open(self.file_new, "r") as file:
                text = ""
                while self.ind != -1:
                    file.seek(self.ind)
                    txt = file.read(1)
                    if txt != self.symbol:
                        text += txt
                    else:
                        self.ind = file.tell()
                        return text
                    self.ind += 1
                # else:
                #     raise StopIteration
        except:
            print("****")

c = IterRead("text8.txt", "~")
for i in c:
    print(i)
    print("===============")