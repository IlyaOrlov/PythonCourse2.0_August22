def fun(a, b):
    print(a + b)


print_result = None

def mock_print(res):
    global print_result
    print_result = res

class Backup:
    def __enter__(self):
        self._bkp = print

    def __exit__(self, exc_type, exc_val, exc_tb):
        global print
        print = self._bkp


with Backup():
    print = mock_print
    fun(10, 20)
    assert print_result == 30
print("The end")