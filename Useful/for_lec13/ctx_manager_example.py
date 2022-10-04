class MyCtxManager:
    def __enter__(self):
        print("Входим в менеджер котекста")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Выходим из менеджера контекста")


with MyCtxManager():
    raise TypeError
    print("Hello")
