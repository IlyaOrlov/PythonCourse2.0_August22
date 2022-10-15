# * Реализовать систему, эмулирующую работу с банкоматами. Создать семейство классов банкоматов, хранящих определенные
# суммы и поддерживающих различные операции (одни банкоматы принимают и выдают наличные, другие позволяют еще и
# проводить онлайн платежи). Операции реализуются посредством методов, выводящих название операции и меняющих
# (при необходимости) количество наличных в банкомате. Для тестирования системы необходимо реализовать алгоритм,
# обходящий список банкоматов разного типа и запрашивающий у каждого банкомата информацию о количестве наличных и
# наборе поддерживаемых операций.


class ATM:

    def __init__(self, title, cash):
        self._cash = cash
        self.title = title

    @property
    def cash(self):
        return self._cash

    @cash.setter
    def cash(self, value):
        res = self._cash + value
        if res > 0:
            self._cash = res
        else:
            print("В банкомате недостаточно средств для совершения операции")

    def show(self):
        y = "пополнение или снятие"
        x = "онлайн-платежи"
        if "pay" in self.__dir__():
            print(f"{self.title} выполняет {x}")
        else:
            print(f"{self.title} выполняет {y}")
        print(f"В банкомате {self.title}: {self._cash}. ")


class Bank1(ATM):
    def __init__(self, title, cash):
        super().__init__(title, cash)

    def pay(self):
        a = int(input("Введите сумму для совершения покупки: "))
        if a > self._cash:
                print("На вашем счете недостаточно средств")
        else:
            self._cash -= a
            print(f"Покупка успешно совершена, списано: {a}")


class Bank2(ATM):
    def __init__(self, title, cash):
        super().__init__(title, cash)

    def operation(self):
        b = int(input("Выберите: 1 - снять, 2 - внести  "))
        if b == 1:
            a = int(input("Введите сумму для снятия со счета: "))
            if a > self._cash:
                print("На вашем счете недостаточно средств")
            else:
                self._cash -= a
                print(f"Со счета списано: {a}, остаток {self._cash}")
        elif b == 2:
            a = int(input("Введите сумму для пополнения счета: "))
            self._cash += a
            print(f"Внесено: {a}, остаток {self._cash}")
        else:
            print("Некорректный ввод")


b1 = Bank1("Bank_1", 5000)
b2 = Bank2("Bank_2", 1000)
b1.show()
b1.pay()
b2.show()
b2.operation()
