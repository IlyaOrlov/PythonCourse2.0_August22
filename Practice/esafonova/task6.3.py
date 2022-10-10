import os
import tempfile

class WrapStrToFIle: # Написать класс WrapStrToFIle
    def __init__(self):
        self._filepath = tempfile.mktemp() #В конструкторе класс должен инициализовать атрибут filepath, путем присваивания результата функции mktemp   библиотеки tempfile.

    @property #который будет иметь одно вычисляемое свойство (property) под названием content.
    def content(self):
        try: # Если файл не существует, то возникает ошибка, поэтому должна быть обертка вокруг открытия файла на чтение (try...except),
            with open(self._filepath, "r") as self.a: # При попытке чтения свойства content должен внутри кода свойства открываться файл,
                return self.a.read() ## используя атрибут filepath (с помощью функции open, из этого файла читается все содержимое и возвращается из свойства.
        except FileNotFoundError:
            print('Файл еще не существует') #с помощью которого будет возвращаться 'Файл еще не существует'.


    @content.setter
    def content(self, value):
        self.value = value
        with open(self._filepath, "w") as self.a: # При присваивании значения свойству content файл по указанному пути
            self.a.write(self.value)# должен открываться  на запись и записываться содержимое.

    @content.deleter
    def content(self):
        os.remove(self._filepath) # При удалении атрибута content, должен удаляться и файл.*


b = WrapStrToFIle()
print(b.content)
b.content = 'Привет'
print(b.content)
del b.content
print(b.content)