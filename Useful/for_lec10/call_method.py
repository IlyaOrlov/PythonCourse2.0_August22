class MyClass:
    def __call__(self, x, y):
        self._x = x
        self._y = y
        self._res = x + y
        return self._res

    def show_last_operation(self):
        print(f"{self._x} + {self._y} = {self._res}")


m = MyClass()

print(m(10, 20))
m.show_last_operation()

print(m(100, 200))
m.show_last_operation()