class Bank:
    def __init__(self, cash):
        self._cash = cash


class Bankomat1(Bank):
    def input_output(self):
        while True:
            inp = input('Внести деньги - введите "1". Для снятия - "2" ')
            if inp.lower() == '1':
                inp = int(input('Положите купюры в лоток: '))
                self._cash += inp
            elif inp.lower() == '2':
                out = int(input('Введите требуемую сумму: '))
                if self._cash < out:
                    print('=== Не достаточно денег в банкомате ===')
                    continue
                self._cash -= out
            else:
                print('----- Неправильный ввод.-----\n '
                      'Для выхода введите: EXIT \n'
                      'Для продолжения операции введите любой знак: ')
                stop = input('---- ')
                if stop.lower() == 'exit':
                    print('Выход')
                    break
                continue
        print(f'Оставшаяся наличность в Bankomat1 : {self._cash}')


class Bankomat2(Bank):
    def exchange(self):
        print(f'Оставшаяся наличность в Bankomat2: {self._cash}')


class Bankomat3(Bank):
    def transfer(self):
        print(f'Оставшаяся наличность в Bankomat3: {self._cash}')


#lst = Bank(1000)
lst1 = Bankomat1(500)
lst2 = Bankomat2(1500)
lst3 = Bankomat3(3000)

lst1.input_output()
lst2.exchange()
lst3.transfer()