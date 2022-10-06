import os
import tempfile


class WrapStrToFile:
    def __init__(self):
        self._path = tempfile.mktemp()  # здесь инициализируется атрибут filepath, он содержит путь до файла-хранилища


    @property
    def content(self):
        try:
            with open(self._path, "r") as f:
                res = f.read()
                return res
        except:
            return "File doesn't exist"

        # попытка чтения из файла, в случае успеха возвращаем содержимое
        # в случае неудачи возвращаем 'File doesn't exist'

    @content.setter
    def content(self, value):
        with open(self._path, "w") as f:
            f.write(value)
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
