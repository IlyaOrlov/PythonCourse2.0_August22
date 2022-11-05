class PerTer:
    _account = [0]

    def __init__(self, name, cash):
        self.name = name
        self._cash = cash

    @property
    def cash(self):
        return self._cash

    @cash.setter
    def cash(self, value):
        if type(self._cash) is not int:
            print("В терминале отсутствует функция пополнения")
        if type(value) is int:
            self._cash += value
        else:
            print("Введео некорректное число")

    def show_info(self):
        met = []
        for j in self.__dir__():
            if j[0] != "_" and j != 'show_info':
                met.append(j)
        print("------------")
        print(f"наличные в терминале {self.name}: {self._cash}")
        print(met)


class Terminal(PerTer):
    def __init__(self, name):
        super().__init__(name, None)


    def check_acc(self):
        print(f"На вашем счету: {self._account[0]}")


class Banckomat(PerTer):
    def __init__(self, name, cash):
        super().__init__(name, cash)

    def replenish(self):
        a = input("Вставьте купюры в купюроприёмник")
        if not a.isdecimal():
            print("Введена некорректная сумма")
        else:
            a = int(a)
            self._account[0] += a
            self._cash += a

    def withdrawal(self):
        a = input("Введите необходимую сумму")
        if not a.isdecimal():
            print("Введена некорректная сумма")
        else:
            a = int(a)
            if a > self._cash:
                print(f"Максимально возможная к выдаче сумма: {self._cash}")
            elif a > self._account[0]:
                print("На Вашем счету недостаточно средств")
            else:
                self._cash -= a
                self._account[0] -= a
                print(f"На Вашем счету осталось: {self._account[0]}")


class Acquiring(PerTer):
    def __init__(self, name):
        super().__init__(name, 0)

    def pay(self):
        a = input("Введите сумму покупки")
        if not a.isdecimal():
            print("Введена некорректная сумма")
        else:
            a = int(a)
            if a > self._account[0]:
                print("На Вашем счету недостаточно средств")
            else:
                self._account[0] -= a
                self._cash += a
                print(f"\nС Вашего счёта списано: {a}\n")
                print("Ваш чек\n")
                print("Благодарим за покупку\n")


b1 = Terminal("Terminal")
b2 = Banckomat("Banckomat", 100000)
b3 = Acquiring("Acquiring")


b2.replenish()
print()
b2.withdrawal()
print()
b1.check_acc()
print()
b3.pay()
print()
b1.check_acc()



lst = [b1, b2, b3]
for i in lst:
    i.show_info()
