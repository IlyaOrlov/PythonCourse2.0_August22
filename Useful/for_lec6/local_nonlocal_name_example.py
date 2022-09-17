def employee(name):
    def name_and_salary(salary):
        nonlocal name
        print(f"my name is: {name}, my salary is {salary}")
        name = "Unknown"

    name_and_salary(100000)
    print(f"my name is {name}")


name = "John"
employee(name)
print(f"Global name: {name}")
