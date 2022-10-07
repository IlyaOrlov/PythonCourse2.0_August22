class BaseClass:
    def get_money(self, value):
        pass

    @classmethod
    def show_operations(cls):
        return [operation for operation in dir(cls) if not operation.startswith('_')]


class MyClass(BaseClass):
    def get_money(self, value):
        pass

    def set_money(self, value):
        pass

    def online_payment(self, value):
        pass


m1 = BaseClass()
m2 = MyClass()

print(m1.show_operations())
print(m2.show_operations())
