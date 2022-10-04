class Bankomat:

    option_lst = ('Операции с наличностью',)
    def __init__(self, name, quantity_cash):
        self._name = name
        self._quantity_cash = quantity_cash

    @property
    def quantity_cash(self):
        return self._quantity_cash

    def inner_menu(self):
        choice_user = input('Выберите операцию 1 - внести 2 - снять: ')
        if choice_user == '1':
            cash_in = int(input('Какую сумму вы хотите внести: '))
            self._quantity_cash += cash_in
            print(f'Операция успешно завершена. Вы внесли {cash_in}')
        elif choice_user == '2':
            cash_out = int(input('Какую сумму вы хотите снять: '))
            if self._quantity_cash < cash_out:
                print('Извините в банкомате недостаточно средств')
            else:
                self._quantity_cash -= cash_out
                print('Операция успешно завершена, не забудьте деньги и карточку')

    @classmethod
    def servisce_atm(cls, all_atm):
        servisce_choice = input('1 - Деньги в банкоматах\n2 - Поддерживаемые операции\nВыберите операцию: ')
        if servisce_choice == '1':
            for i in range(len(all_atm)):
                print(f'В банкомате {all_atm[i]._name} наличности {all_atm[i]._quantity_cash}')
        else:
            for i in cls.option_lst:
                print(i, end=', ')
            print()


    def menu(self, choice_user, choice_ATM, all_atm):
        if choice_user == 1:
            self.inner_menu()
        elif choice_user == 2:
            if choice_ATM == 1:
                print('Данный банкомат не принимает платежи')
            else:
                self.online_pay()
        else:
            servisce_pass = int(input('Введите сервисный пароль: '))  # Супер секретный пароль: 123
            if servisce_pass == 123:
                self.servisce_atm(all_atm)
            else:
                print('Не верный пароль')

class BankomatOnLine(Bankomat):
    option_lst = Bankomat.option_lst + ('онлайн платежи',)

    @staticmethod
    def online_pay():
        _ = input('1 - Сотовый телефон\n2 - ЖКХ\nВыберите платеж: ')
        print('Платеж принят')

ATM_machine_1 = Bankomat('niz_b_1', 500000)
ATM_machine_2 = BankomatOnLine('niz_b_2', 750000)
ATM_machine_3 = BankomatOnLine('niz_b_3', 250000)
ATM_machine_4 = Bankomat('niz_b_4', 300000)
all_atm = (ATM_machine_1, ATM_machine_2, ATM_machine_3, ATM_machine_4)

choice_ATM = int(input('1 - Без возможности платежей\n2 - С возможностью платежей\nВыберите банкомат:  '))
choice_user = int(input('1 - Операции с наличностью\n2 - Онлайн платежи\n3 - Сервисное меню\nВыберите операцию: '))
if choice_ATM == 1:
    ATM_machine_1.menu(choice_user, choice_ATM, all_atm)
else:
    ATM_machine_2.menu(choice_user, choice_ATM, all_atm)





