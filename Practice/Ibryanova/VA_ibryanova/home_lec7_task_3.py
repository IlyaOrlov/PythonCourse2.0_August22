import tempfile
import os


class WrapStrToFile:

    def __init__(self):
        self.filepath = tempfile.mktemp()

# здесь инициализируется атрибут filepath, он содержит путь до файла-хранилища

    @property
    def content(self):
        try:
            with open(self.filepath, 'r') as f:
                res = f.read()
                f.close()
                return res
        except:
            return 'Файл еще не существует'


    # попытка чтения из файла, в случае успеха возвращаем содержимое

    # в случае неудачи возвращаем 'File doesn't exist'

    @content.setter
    def content(self, value):
        with open(self.filepath, 'w') as f:
            f.write(value)
            f.close()

    # попытка записи в файл указанного содержимого

    @content.deleter
    def content(self):
        os.remove(self.filepath)


# удаляем файл: os.remove(имя_файла)


wstf = WrapStrToFile()
print(wstf.content)  # Output: File doesn't exist
wstf.content = 'test str'
print(wstf.content)  # Output: test_str
wstf.content = 'text 2'
print(wstf.content)  # Output: text 2
del wstf.content  # после этого файла не существует