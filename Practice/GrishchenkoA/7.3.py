# -*- coding: utf-8 -*-
class ATM:
    def __init__(self, cash):
        self._cash = cash

        def get_cash(self):
            return self._cash

        def set_cash(self, name):
            self._cash = cash


class SimpleATM(ATM):
    def deposit_cash(money):
        if type(money) is float:
            return money
        else:
            print("Неверно введена сумма")
    def choice(self):
        request = input("Выберите желаемую операцию: 1 - если хотите внести наличные, 2 - если хотите снять наличные: ")
        if request == "1":
            money = float(input("Введите сумму для внесения наличных на счет: "))
            self._cash = self._cash + money
            print(f"На вашем счету теперь: {self._cash} рублей")
        if request == "2":
            money = float(input("Введите сумму, которую хотите снять со счета: "))
            if self._cash < money:
                print("Недостаточно средств на счете")
            else:
                self._cash = self._cash - money
                print(f"На вашем счету теперь: {self._cash} рублей")
        return self._cash


class SuperATM(ATM):
    def choice(self):
        request = input("Выберите желаемую операцию: 1 - если хотите внести наличные, 2 - если хотите снять наличные, 3 - хотите оплатить онлайн: ")
        if request == "1":
            money = float(input("Введите сумму для внесения наличных на счет: "))
            self._cash = self._cash + money
            print(f"На вашем счету теперь: {self._cash} рублей")
        if request == "2":
            money = float(input("Введите сумму, которую хотите снять со счета: "))
            if self._cash < money:
                print("Недостаточно средств на счете")
            else:
                self._cash = self._cash - money
                print(f"На вашем счету теперь: {self._cash} рублей")
        if request == "3":
            money = float(input("Введите сумму для оплаты онлайн: "))
            if self._cash < money:
                print("Недостаточно средств на счете")
            else:
                self._cash = self._cash - money
                print(f"На вашем счету теперь: {self._cash} рублей")
        return self._cash


# person_1 = SimpleATM(50000)
# person_1.choice()

person_2 = SuperATM(52000)
person_2.choice()





