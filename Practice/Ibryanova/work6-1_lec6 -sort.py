class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def __str__(self):
        return f'Сотрудник: {self.name} {self.surname} '


    def __repr__(self):
        return f'Сотрудник: {self.name} {self.surname} с з/п {self.salary}'


    def show(self):
        print(f'Сотрудник: {self.name} {self.surname} с з/п {self.salary}')

    def __lt__(self, other):
        print(self)
        print(other)
        if self.surname == other.surname:
            return self.name < other.name
        else:
            return self.surname < other.surname

#       def __le__(self, other):
#            print(self)
#            print(other)
#            if self.surname == other.surname:
#                return self.name <= other.name
#            else:
#                return self.surname < other.surname

e1 = Employee('Anton', 'Antonov', 150000)
e2 = Employee('Ivan', 'Antonov', 130000)

print(e1 < e2 # Employee.e1.__lt__(e2)

#lst = [
 #   Employee('Petr', 'Petrov', 100000), Employee('Anton', 'Antonov', 150000),
#    Employee('Ivan', 'Ivanov', 120000), Employee('Ivan', 'Antonov', 130000)]


#lst.sort()# можем отсортировать сотр-ов по фамилии
#print(lst)