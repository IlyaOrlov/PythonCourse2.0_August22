import os
import tempfile


class WrapStrToFile:
    def __init__(self):
        self._path = tempfile.mktemp()  # здесь инициализируется атрибут filepath, он содержит путь до файла-хранилища

    @property
    def content(self):
        try:
            f = open(self._path, "r")
        except:
            return "File doesn't exist"
        else:
            res = f.read()
            f.close()
            return res

        # попытка чтения из файла, в случае успеха возвращаем содержимое
        # в случае неудачи возвращаем 'File doesn't exist'

    @content.setter
    def content(self, value):
        f = open(self._path, "w")
        f.write(value)
        f.close()
        # попытка записи в файл указанного содержимого

    @content.deleter
    def content(self):
        os.remove(self._path)
        # удаляем файл: os.remove(имя_файла)


wstf = WrapStrToFile()
print(wstf.content)  # Output: File doesn't exist
wstf.content = 'test str'
print(wstf.content)  # Output: test_str
wstf.content = 'text 2'
print(wstf.content)  # Output: text 2
