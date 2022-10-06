import contextlib

@contextlib.contextmanager
def my_ctx_manager():
    try:
        print("On enter")
        yield
    finally:
        print("On exit")

class MyCtxManager:
    def __enter__(self):
        print("On enter")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("On exit")

with my_ctx_manager():
    print("Hello")

with MyCtxManager():
    print("Hello")