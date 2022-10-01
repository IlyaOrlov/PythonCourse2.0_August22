class Terminal:
    _account = [0]
    _cash = "Терминал не хранит наличные"

    def __init__(self, name):
        self._name = name

    def check_acc(self):
        print(f"На вашем счету: {self._account[0]}")

    @property
    def cash(self):
        return self._cash

    @cash.setter
    def cash(self, value):
        if type(value) is int:
            self._cash += value
        else:
            print("Введео некорректное число")


class Banckomat(Terminal):

    def __init__(self, name, cash):
        Terminal.__init__(self, name)
        self._cash = cash

    def replenish(self):
        a = input("Вставьте купюры в купюроприёмник")
        if not a.isdecimal():
            print("Введена некорректная сумма")
        else:
            a = int(a)
            self._account[0]+=a
            self._cash+=a

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


class Acquiring(Terminal):
    _cash = 0

    def pay(self):
        a = input("Введите сумму покупки")
        if not a.isdecimal():
            print("Введена некорректная сумма")
        else:
            a = int(a)
            if a > self._account[0]:
                print("На Вашем счету недостаточно средств")
            else:
                self._account[0]-=a
                self._cash +=a
                print(f"С Вашего счёта списано: {a}")
                print("Ваш чек")
                print("Благодарим за покупку")
    @staticmethod
    def check_acc():
        print(f"Терминал экваринга не располагает информацией о Вашем счёте. Как Вы вообще умудрились вызвать это сообщение?!")


b1 = Terminal("Terminal")
b2 = Banckomat("Banckomat", 100000)
b3 = Acquiring("Acquiring")


b2.replenish()
b2.withdrawal()
b1.check_acc()
b3.pay()
b1.check_acc()
print("==============")


lst = [b1, b2, b3]
for i in lst:
    met=[]
    for j in dir(i):
        if j[0] != "_":
            met.append(j)
    print(i.cash)
    print(met)