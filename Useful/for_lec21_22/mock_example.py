def fun(a, b):
    print((a + b) * 100)


def mock_print(arg):
    mock_print.arg = arg

class CtxMgr:
    def __enter__(self):
        global print
        self.bkp_print = print
        print = mock_print
    def __exit__(self, exc_type, exc_val, exc_tb):
        global print
        print = self.bkp_print

with CtxMgr():
    fun(1, 2)

assert(mock_print.arg == 300)
print(mock_print.arg)


