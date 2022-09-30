class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def __str__(self):
        return f"Сотрудник {self.name} {self.surname}"

    def __repr__(self):
        return f"Сотрудник {self.name} {self.surname} с з/п {self.salary}"

    def __lt__(self, other):
        if self.surname == other.surname:
            return self.name < other.name
        else:
            return self.surname < other.surname

    def __le__(self, other):
        if self.surname == other.surname:
            return self.name <= other.name
        else:
            return self.surname < other.surname

    def show(self):
        print(f"Сотрудник {self.name} {self.surname} с з/п {self.salary}")


e1 = Employee("Anton", "Antonov", 130000)
e2 = Employee("Ivan", "Antonov", 130000)

print(e1 <= e2)  # Employee.__lt__(e2, e1)

# lst = [
#     Employee("Ivan", "Ivanov", 100000), Employee("Petr", "Petrov", 150000),
#     Employee("Anton", "Antonov", 130000), Employee("Ivan", "Antonov", 130000)
# ]
# lst.sort()
# print(lst)