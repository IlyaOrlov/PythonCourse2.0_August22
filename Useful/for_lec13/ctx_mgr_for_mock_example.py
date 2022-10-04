def fun(a, b):
    print(a + b)


def mock_print(arg):
    mock_print.attr = arg


class MyCtx:
    def __enter__(self):
        global print
        self.old_print = print
        print = mock_print

    def __exit__(self, exc_type, exc_val, exc_tb):
        global print
        print = self.old_print


with MyCtx():
    fun(10, 20)

print(mock_print.attr)
assert(mock_print.attr == 30)