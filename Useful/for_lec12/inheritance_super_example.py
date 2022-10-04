class Employee:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def __str__(self):
        return f"{type(self).__name__}: {self._first_name} {self._last_name}"


class Manager(Employee):
    def __init__(self, first_name, last_name, emp_lst):
        super().__init__(first_name, last_name)
        self._employees = emp_lst


e1 = Employee("Petr", "Petrov")
print(e1)

m1 = Manager("Ivan", "Ivanov", (e1, ))
print(m1)
