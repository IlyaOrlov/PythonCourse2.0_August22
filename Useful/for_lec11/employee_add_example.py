class Employee:
    def __init__(self, n, s, salary):
        self.name = n
        self.surname = s
        self.salary = salary

    def __add__(self, other):
        return Employee("", "", self.salary + other.salary)


e1 = Employee("Ivan", "Ivanov", 100000)
e2 = Employee("Petr", "Ivanov", 200000)
e3 = Employee("Semen", "Ivanov", 150000)


res = e1 + e2 + e3
print(res.salary)
