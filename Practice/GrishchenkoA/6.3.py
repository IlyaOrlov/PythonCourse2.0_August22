import tempfile
import os


class WrapStrToFile:
    def __init__(self):
        self.filepath = tempfile.mktemp()


    @property
    def content(self):
        try:
            with open(self.filepath, "r") as readfile:
                file_1 = readfile.read()
                return file_1
        except:
            return "File doesn't exist"


    @content.setter
    def content(self, value):
        try:
            with open(self.filepath, "w") as writefile:
                writefile.write(value)
        except:
            return "Error writing to file"


    @content.deleter
    def content(self):
        os.remove(self.filepath)


wstf = WrapStrToFile()
print(wstf.content)
wstf.content = 'test str'
print(wstf.content)
wstf.content = 'text 2'
print(wstf.content)
del wstf.content
