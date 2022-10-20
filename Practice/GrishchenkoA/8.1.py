# -*- coding: utf-8 -*-
class IterRead:
    def __init__(self, file_new, symbol):
        self.file_new = file_new
        self.symbol = symbol
        self.ind = 0


    def __iter__(self):
        return self

    def __next__(self):
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
            if txt == "":
                raise StopIteration

    def __del__(self):
        self.file_new()


with open("text1.txt", "r") as file:
    for i in IterRead(file, "~"):
        print(i)
        print("===============")