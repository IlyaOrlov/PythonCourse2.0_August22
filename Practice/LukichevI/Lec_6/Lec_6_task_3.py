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


wstf = WrapStrToFile()
print(wstf.content)  # Output: File doesn't exist
wstf.content = 'test str'
print(wstf.content)  # Output: test_str
wstf.content = 'text 2'
print(wstf.content)  # Output: text 2
del wstf.content     # после этого файла не существует
