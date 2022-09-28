class BaseEmployee:
    num = 0

    def __init__(self):
        BaseEmployee.num += 1


class Employee(BaseEmployee):
    num = 0

    def __init__(self):
        Employee.num += 1


class Manager(BaseEmployee):
    num = 0

    def __init__(self):
        Manager.num += 1


e1 = Employee()
e2 = Employee()
m = Manager()
print(f"{Employee.num=}")
print(f"{Manager.num=}")