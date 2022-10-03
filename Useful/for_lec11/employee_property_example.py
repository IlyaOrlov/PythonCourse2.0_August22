class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self._salary = salary

    def __lt__(self, other):
        return self._salary < other._salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if type(new_salary) is int:
            self._salary = new_salary
        else:
            print("Incorrect salary")

    def show(self):
        print(f"Сотрудник {self.name} {self.surname} с з/п {self._salary}")


e1 = Employee("Anton", "Antonov", 130000)
e2 = Employee("Ivan", "Antonov", 150000)
e1.show()
e2.show()
print(e1 < e2)
print("=======================")
# e1.set_salary(e1.get_salary() + 20000)
e1.salary += 20000  # e1.salary = e1.salary + 20000
e2.salary = "100000"
e1.show()
e2.show()
print(e1 < e2)
