# Написать класс-обертку над SQLite (с возможностями менеджера контекста),
# которая может на вход принимать строки SQL запросов и возвращать данные в формате json.
# Класс должен иметь, как минимум, методы select и execute.
import sqlite3


class MySQLite:

    def __init__(self, path):
        self._path = path
        self._name_table = None

# Методы my_execute_values, enter, exit и все методы связанные с ними были написаны мной до того как я задал Вам вопрос.
# Мне было просто очень жаль удалять их, поэтому я их оставил...
# Тем более, что до этого написал неправильный, но рабочий код на 100+ строк и удалил :(
# Можете, пожалуйста, глянуть эти методы и сказать что с ними не так? Они не избыточны?
# Стоит избегать таких длинных методов в практике?

    def my_execute_values(self):
        self._name_table = self._choice_tabl()
        if not self._name_table:
            print("В базе данных не существует таблиц. Невозможно установить значения.")
            return None
        columns = self._cur.execute(f"SELECT * FROM {self._name_table}").description
        columns = tuple([i[0] for i in columns])
        print(f"В таблице {self._name_table} содержатся столбцы: {columns}")
        values = []
        for i in columns:
            value = input(f"Введите значение для столбца {i}")
            values.append(value)
        values = tuple(values)
        self._database.execute(f"INSERT INTO {self._name_table}{str(columns)}VALUES {str(values)}")

    def _choice_tabl(self):
        # скрипт выбирает таблицу по умолчанию, для работы с ней внутри my_execute_values()
        name_table = self._cur.execute("SELECT name from sqlite_master where type= 'table'").fetchall()
        len_list_name = len(name_table)
        match len_list_name:
            case 0:
                return None
            case 1:
                return name_table[0][0]
            case _:
                while True:
                    name = input(f"В базе данных более одной таблицы. Список таблиц: {name_table}\n"
                                 f"Выберете таблицу с которой будут происходить дальнейшие операции: ")
                    if name in name_table:
                        return name
                    else:
                        print("Выбор непонятен")

    def my_execute(self, s):
        if not self.proverka(s, ["INSERT", "UPDATE", "DELETE"]):
            print("Неверная команда. Метод my_execute не возвращает значение")
            return None
        self._cur.execute(s)
        self._database.commit()

    def my_select(self, s, mod=None):
        if not self.proverka(s, ["SELECT"]):
            print("Неверная команда. Метод my_select возвращает значение и не сохраняет изменения в базе данных")
            return None
        res = self._cur.execute(s)
        if mod:
            res = self._mod(mod, res)
        if type(res) is sqlite3.Cursor:
            res = res.description
        return res

    @staticmethod
    def _mod(mod, res):
        match mod:
            case "fa":
                res = res.fetchall()
            case "fo":
                res = res.fetchone()
            case "fm":
                while True:
                    size = input("Введите максимальный размер выводимых данных, "
                                 "или нажмите Enter для значения по умолчанию(1): ")
                    if size.isdecimal():
                        size = int(size)
                        break
                    elif size == "":
                        size = 1
                        break
                    else:
                        continue
                res = res.fetchmany(size)
            case _:
                print("Неверно указан модификатор")
                return None
        return res

    @staticmethod
    def proverka(com, lst_com):
        for i in lst_com:
            if i in com:
                break
        else:
            return False
        return True

    def __enter__(self):
        self._database = sqlite3.connect(self._path)
        self._cur = self._database.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        while True:
            reply = input("Сохранить базу данных?(y/n)")
            match reply:
                case "y":
                    self._database.commit()
                    break
                case "n":
                    break
                case _:
                    print("Выбор непонятен")
        self._database.close()


base = MySQLite("MyDataBase.db")
with base:
    base.my_execute("SELECT * FROM l")# Не выполнится
    print(base.my_select("SELECT name from sqlite_master where type= 'table'", mod="fa"))
    tabl_name = base.my_select("SELECT name from sqlite_master where type= 'table'", mod="fo")
    print(base.my_select("SELECT name from sqlite_master where type= 'table'", mod="fm"))
    if tabl_name:
        print(base.my_select(f"SELECT * FROM {tabl_name[0]}"))


