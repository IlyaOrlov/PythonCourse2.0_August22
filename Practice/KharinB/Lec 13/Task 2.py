# Написать скрипт, работающий под SQLite/MySQL/PostgreSQL, который создает 3 сущности:
# производители, покупатели, товары. Необходимо добавить демо-данные и выполнить следующие выборки:
# вывести все товары с указанием информации о производителе
# найти все товары, которые никто не покупал
import sqlite3
import random
import os


class MyDB:

    def __init__(self, path):
        self._path = path
        self._company = ["Кштымский Автозавод", "Autodesk", "HP", "Xaomi"]
        self._name = ["Леопольд", "Матильда", "Иван", "Элеонора"]
        self._title = [("Подшипники", "Пятое колесо"), ("3D max", "AutoCAD"), ("Принтер", "Ноутбук"),
                        ("Смартфон", "Самокат")]
        self._city = ["Кштымск", "Сан_Рафаэль", "Пало-Альто", "Пекин"]

    def my_select(self, s):
        return self._cur.execute(s).fetchall()

    def company_product(self):
        self._cur.execute("SELECT product.id, title, manufacturer.company, manufacturer.city FROM product "
                          "JOIN manufacturer ON manufacturer.company=product.company")
        a = self._cur.fetchone()
        while a:
            print(a)
            a = self._cur.fetchone()

    def not_bought(self):
        res = self._cur.execute("select title from product except select product from buyer").fetchall()
        return res

    def __enter__(self):
        self._database = sqlite3.connect(self._path)
        self._cur = self._database.cursor()
        self._create_db()

    def _create_db(self):
        self._database.execute("CREATE TABLE manufacturer"
                               "    (id       INT  PRIMARY KEY NOT NULL,"
                               "     company  TEXT             NOT NULL,"
                               "     city     TEXT                     );")
        self._database.execute("CREATE TABLE buyer"
                               "    (id       INT  PRIMARY KEY NOT NULL,"
                               "     product  TEXT             NOT NULL,"
                               "     name     TEXT             NOT NULL);")
        self._database.execute("CREATE TABLE product"
                               "    (id       INT  PRIMARY KEY NOT NULL,"
                               "     title    TEXT             NOT NULL,"
                               "     company  TEXT             NOT NULL);")
        self._data_choice()

    def _data_choice(self):
        id = 1
        for id_com in range(len(self._company)):
            value = str(id_com+1), self._company[id_com], self._city[id_com]
            self._database.execute(f"INSERT INTO manufacturer (id, company, city)VALUES( ?, ?, ?);", value)
            for product_n in range(2):
                value = str(id), self._title[id_com][product_n], self._company[id_com]
                self._database.execute(f"INSERT INTO product (id, title, company)""VALUES (?, ?, ?);", value)
                id += 1
        for sales in range(1, random.randint(3,8)):
            product = random.choice(self._title)[random.choice((0, 1))]
            name = random.choice(self._name)
            value = str(sales), product, name
            self._database.execute("INSERT INTO buyer (id, product, name)VALUES (?, ?, ?);", value)

    def __exit__(self, exc_type, exc_val, exc_tb):
        while True:
            reply = input("Сохранить базу данных?(y/n)")
            match reply:
                case "y":
                    self._database.commit()
                    self._database.close()
                    break
                case "n":
                    self._database.close()
                    os.remove(self._path)
                    break
                case _:
                    print("Выбор непонятен")




base = MyDB("MyData.db")
with base:
    print("Сводная таблица продуктов и информации о производителе:")
    base.company_product()
    print("=================================================")
    print(f"Товары небыли куплены: {base.not_bought()}")
    pass
