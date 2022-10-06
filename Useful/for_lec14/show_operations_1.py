class BaseClass:
    _operations = ("Приём наличных",)

    @classmethod
    def show_operations(cls):
        return cls._operations


    


class MyClass(BaseClass):
    _operations = ("Выдача наличных", "Приём наличных", "Онлайн платежи")


m1 = BaseClass()
m2 = MyClass()

print(m1.show_operations())

print(m2.show_operations())
