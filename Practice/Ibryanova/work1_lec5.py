#def fun(x):
#    x = 100
#   print(f'Local x: {x}')


#x = 1000
#fun(x)
#print(f'Global x: {x}')


#def emploee(name):
#    def name_and_salary(salary):
#       nonlocal name
#       print(f'my name is: {name}, my salary is: {salary}')
#       name = 'Unknow'
#
#   name_and_salary(100000)
#   print(f'my name is: {name}')
#
#name = 'John'
#emploee(name)
#print(f'Global name" {name}')


# еще пример нелокальной обл

def fun():
    def inner_fun():
        print(f'local x: {x}')

    x = 100
    inner_fun()
    print(f'Nonlocal x: {x}')


x = 1000
fun()
print(f'Global x: {x}')








