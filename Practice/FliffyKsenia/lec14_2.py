import sqlite3
import random

conn = sqlite3.connect("lec14_2.db")  # подключаемся к базе
cursor = conn.cursor()


def createdb():  # функция создания таблиц и заполнение данными
    cursor.execute(  # создаем таблицу производителей у которых мы знаем только имя.
        "CREATE TABLE IF NOT EXISTS manufacturers (Manufacturersid INTEGER PRIMARY KEY AUTOINCREMENT, name text)")
    manufactors = ['adidas', 'nike  ', 'noname']  # вводим список для заполения таблицы производителей
    for m in manufactors:  # заполняем таблицу производителей в цикле.
        cursor.execute(f"insert into manufacturers (name) values ('{m}')")

    cursor.execute(  # создаем таблицу покупателей у них мы знаем возраст и имя.
        "CREATE TABLE IF NOT EXISTS buyers (buyersid INTEGER PRIMARY KEY AUTOINCREMENT, name text, age integer)")
    buyers = [['John', 25], ['Mary', 27], ['Barak', 47]]  # создаем список для заполнения таблицы покупателей
    for b in buyers:  # заполняем таблицу покупателей
        cursor.execute(f"insert into buyers (name,age) values ('{b[0]}',{b[1]})")

    cursor.execute(  # создаем таблицу продуктов
        "CREATE TABLE IF NOT EXISTS products (productid INTEGER PRIMARY KEY AUTOINCREMENT, Manufacturersid INTEGER, name text)")
    products = [[1, "Олимпийка"], [2, 'Кросовки'], [3, 'Ремень'],
                [1, 'Неликвид']]  # создаем список для заполения таблицы продуктов
    for pr in products:  # заполняем таблицу продуктов.
        cursor.execute(f"insert into products (Manufacturersid, name) values ({pr[0]},'{pr[1]}')")

    cursor.execute(  # создаем таблицу покупок
        "CREATE TABLE IF NOT EXISTS purchases (purchasesid INTEGER PRIMARY KEY AUTOINCREMENT, buyersid INTEGER, productid INTEGER, price float, quantity float)")

    for pu in range(15):
        cursor.execute(
            # заполняем таблицу покупок. так как нам надо вывести, те товары которые никто не покупал, в рандоме для йд товара не участвует цифра 4. чтобы ее точно никто не купил.
            f"insert into purchases (buyersid, productid, price, quantity) values ({random.randint(1, 3)},{random.randint(1, 3)},{random.randint(0, 90)},{random.randint(1, 90)})")

    conn.commit()  # подтверждаем транзакцию изменения базы.


if __name__ == '__main__':
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='manufacturers'")
    if cursor.fetchall() == []:  # проверяем есть ли таблица "manufacturers", если нет, то считаем, что нет всех таблиц из запускаем функцию создания таблиц.
        createdb()
    print("Все товары:")
    cursor.execute(
        "select p.name,m.name from products p, manufacturers m where p.Manufacturersid = m.Manufacturersid ")  # запрос для выборки всех товаров с производиелями
    print("Производитель | Модель")
    print("--------------|------------")
    for fet in cursor.fetchall():
        print(f"   {fet[1]}     | {fet[0]}")

    print("")
    print("Не популярные товары:")
    print("Производитель | Модель")
    print("--------------|------------")
    cursor.execute(
        "select p.name,m.name from products p, manufacturers m where p.Manufacturersid = m.Manufacturersid and p.productid not in (select productid from purchases)")  # запрос для выборки непопулярных товаров.
    for fet in cursor.fetchall():
        print(f"   {fet[1]}     | {fet[0]}")
