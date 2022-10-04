class Employee:
    def __init__(self, name, salary, info):
        self._name = name
        self._salary = salary
        self._info = info


class Manager(Employee):
    def __init__(self, name, salary, info):
        super().__init__(name, salary, info)
        self._employees = []


class Administrator(Employee):
    pass
