# Реализовать систему, эмулирующую работу с банкоматами. Создать семейство классов банкоматов, хранящих
# определенные суммы и поддерживающих различные операции (одни банкоматы принимают и выдают наличные, другие позволяют
# еще и проводить онлайн платежи). Операции реализуются посредством методов, выводящих название операции и меняющих
# (при необходимости) количество наличных в банкомате. Для тестирования системы необходимо реализовать алгоритм,
# обходящий список банкоматов разного типа и запрашивающий у каждого банкомата информацию о количестве наличных
# и наборе поддерживаемых операций.


class Atm:
    _ability = ["Выдача наличных", "Прием наличных"]

    def __init__(self, cash):
        self._cash = cash

    @property
    def cash(self):
        return self._cash

    @cash.setter
    def cash(self, delta_cash):
        if delta_cash > 0:
            print(f"Пополние успешно на сумму {abs(delta_cash)} у.е.")
            self._cash += delta_cash
        else:
            if abs(delta_cash) > self._cash:
                print(f"В банкомате недостаточно средств")
            else:
                print(f"Выдано наличных на сумму {abs(delta_cash)} у.е.")
                self._cash += delta_cash

    def operations(self):
        for _ in self._ability:
            print(_, end=" ")


class NewAtm(Atm):
    _ability = Atm._ability.copy()
    _ability.append("Онлайн оплата")

    @staticmethod
    def online_banking(self):
        print("Онлайн оплата успешно проведена")


def atm_status(array):
    for i in range(len(array)) :
        print(f"\nATM {i}")
        array[i].operations()
        print(f"\nНаличных внутри {array[i].cash} у.е.")


atm_in_city = [Atm(5000), NewAtm(10000), Atm(4500), Atm(6000)]
atm_status(atm_in_city)
atm_in_city[0].cash = -100000
atm_in_city[2].cash = 2000
atm_status(atm_in_city)
