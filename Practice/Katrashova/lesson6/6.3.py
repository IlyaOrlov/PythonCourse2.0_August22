import tempfile
import os


class WrapStrToFile:
    def __init__(self):
        self._filepath = tempfile.mktemp()

    @property
    def content(self):
        try:
            with open(self._filepath, 'r') as f:
                return f.read()
        except Exception:
            return 'Файл еще не существует'

    @content.setter
    def content(self, value):
        with open(self._filepath, 'w') as f:
            f.write(value)

    @content.deleter
    def content(self):
        os.remove(self._filepath)


a = WrapStrToFile()
print(a.content)  # Output: File doesn't exist
a.content = 'test str'
print(a.content)  # Output: test_str
a.content = 'text 2'
print(a.content)  # Output: text 2
del a.content     # после этого файла не существует
