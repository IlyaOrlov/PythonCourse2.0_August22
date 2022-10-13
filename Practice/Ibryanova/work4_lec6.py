class Employee:
    def __init__(self, name, surname):
        print(self)
        self.name = name
        self.surname = surname
    #name = 'Ivan'
    #surname = 'Ivanov'

#print(Employee.name)
#print(Employee.surname)

#нужно создать объект класса Employee

emp1 = Employee('Petr', 'Petrov')# вместо emp1.name = 'Petr' и emp1.surname = 'Petrov'
#emp1.name = 'Petr'
#emp1.surname = 'Petrov'
#print(type(emp1)) # <class '__main__.Employee'>
#print(emp1.surname)
print(emp1.__dict__)

emp2 = Employee('Anton', 'Antonov')
#emp2.name = 'Anton'
#emp2.surname = 'Antonov'
#print(emp2.name)
#print(emp2.surname)
print(emp2.__dict__)


#print(Employee.name)
#print(Employee.surname)
#print(Employee.__dict__)

lst = [emp1, emp2]
for i in lst:
    print(f'Выдать премию: {i.name} {i.surname}')