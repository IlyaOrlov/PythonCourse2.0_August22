#вызов функции sravnenie (x, t)
def sravnenie(x, t):
    print(max(x,t)) #печать результата сравнения


# вызов функции vozvrat(x, t)
def vozvrat(x, t):
    return max(x, t) #возврат результата сравнения


# вызов на экран функции sravnenie (x, t)
sravnenie(10, 40)
# печать на экране vozvrat(x, t)
print(vozvrat(80, 20))
