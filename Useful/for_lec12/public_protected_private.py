class A:
    def __init__(self):
        self.__attr = 1000

    def pay(self, n):
        self.__attr -= n

# public
# _protected
# __private
a = A()
print(a.__dict__)
print(a._A__attr)