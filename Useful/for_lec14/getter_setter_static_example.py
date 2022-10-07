class MyClass:
    def __init__(self):
        self._attr = 0

    def get_attr(self):
        return self._attr

    def fun(self):
        print(self)

    def fun2(self, other):
        # print(self.__dict__['attr1'] + other.__dict__['attr2'])
        print(n.attr1 + m.attr2)

    @staticmethod
    def method():
        print("Hello")


m = MyClass()
m.attr1 = 10
m.attr2 = 100
print(dir(m))

n = MyClass()
n.attr1 = 30
n.attr2 = 20
# MyClass.fun2(m, n)
m.fun2(n)
n.fun2(m)

MyClass.method()
m.method()
