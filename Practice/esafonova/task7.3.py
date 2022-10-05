# Реализовать систему, эмулирующую работу с банкоматами.
# Создать семейство классов банкоматов, хранящих определенные суммы и поддерживающих различные операции
# (одни банкоматы принимают и выдают наличные, другие позволяют еще и проводить онлайн платежи).
# Операции реализуются посредством методов, выводящих название операции и меняющих (при необходимости) количество наличных
# Для тестирования системы необходимо реализовать алгоритм, обходящий список банкоматов разного типа
# и запрашивающий у каждого банкомата информацию о количестве наличных и наборе поддерживаемых операций.

class ATM:
    def __init__(self, id, storage):
        self.id = id
        self._storage = storage

    @property
    def storage(self):
        return self._storage

    def introduction(self, deposit):
        if not type(self._storage) is int:
            print('Внесение невозможно')
        elif type(deposit) is int:
            self._storage += deposit
        else:
            print('Введена некорректная сумма для внесения!')

    def withdrawal(self, amound):
        if self._storage < amound:
            print('Недостаточно средств')
        elif type(amound) is int:
            self._storage -= amound
        else:
            print('Введена некорректная сумма для снятия')

    def show(self):
        a = []
        a1 = 'Внесение'
        a2 = 'Cнятие'
        a3 = 'Онлайн-платежи'
        for _ in self.__dir__():
            if 'online_pay' in self.__dir__():
                a = a1 + ' ' + a2 + ' ' + a3
                print(a)
                break
            else:
                a = a1 + ' ' + ' ' + a2
                print(a)
                break
        print(f'В банкомате {self.id} хранится: {self._storage}')

class First(ATM):
    def __init__(self, id, storage):
        super().__init__(id, storage)

    def first_introduction(self):
        cash = input('Внесите наличные и введите сумму: ')
        if not cash.isdecimal():
            print('Неправильный ввод')
        else:
            cash = int(cash)
            super().introduction(cash)


    def first_withdrawal(self):
        cash_in = input('Введите сумму для снятия: ')
        if not cash_in.isdecimal():
            print('Неправильный ввод')
        else:
            cash_in = int(cash_in)
            super().withdrawal(cash_in)
            print('Cнятие успешно')

class Next(ATM):
    def __init__(self, id, storage):
        super().__init__(id, storage)

    def online_pay(self):
        cash_online = input('Введите сумму перевода: ')
        if not cash_online.isdecimal():
            print('Неправильный ввод')
        else:
            cash_online = int(cash_online)
            if cash_online > self._storage:
                print('Недостаточно средств')
            else:
                self.self._storage -= cash_online
                print(f'Совершен перевод на сумму: {cash_online}')

bank1 = First("ID_123", 30000)
bank2 = Next("ID_456", 40000)


bank1.first_withdrawal()
print()



lst = [bank1, bank2]
for i in lst:
    i.show()