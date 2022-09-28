class BaseEmployee:
    num = 0

    def __init__(self):
        type(self).inc_num()

    @classmethod
    def inc_num(cls):
        print(cls)
        cls.num += 1


class Employee(BaseEmployee):
    num = 0


class Manager(BaseEmployee):
    num = 0


e1 = Employee()
e2 = Employee()
m = Manager()
print(f"{Employee.num=}")
print(f"{Manager.num=}")