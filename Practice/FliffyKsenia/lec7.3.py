# создаем класс простого банкомата который умеет только выдавать наличку
class Bankomat:
    money = 0
    name = ""
    operations = {"Выдача наличных."}

    # функция выдачи налички
    def vydacha_nal(self, skolco):
        if self.money >= skolco:
            self.money -= skolco
            print(f"Получите свои {skolco} чеканных монет.")
        else:
            print("Извините, но банкомат не распологает требуемой суммой. Попробуйте сократить свои апетиты.")

    # функция инвентарицации выводит имя банкомата количество денег и поддерживаемые операции
    def inventory(self):
        return f"Имя: {self.name}, количество средств: {self.money}, поддерживаемые операции: {self.operations}"

    # функция объявления банкомата обзывает банкомат и начальная сумма.
    def __init__(self, name, cash):
        self.name = name
        self.money = cash

# более продвидутый банкомат умеет к и принимать и выдавать деньги.
class Prostoi_bankomat(Bankomat):
    operations = {"Выдача наличных.", "Прием наличных."}
    def priem_nal(self, skolco):
        self.money += skolco

# Умный банкомат умеет принимать и выдавать деньги, а также проводить онлайн операции.
class Wise_bankomat(Prostoi_bankomat):
    operations = {"Выдача наличных.", "Прием наличных.","Онлайн операции"}
    def online_payment(self):
        print("Онлайн операция проведена! Это было здорово!")

# объевляем список банкоматов различных типов
bankomats = [Bankomat("Первый",5500),Prostoi_bankomat("Второй",6000),Wise_bankomat("Третий",4500)]

# производим обход списка банкоматов и выводим их имена и количесво денег.
for inv in bankomats:
    print(inv.inventory())
