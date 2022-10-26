# 1.Написать класс-обертку над SQLite (с возможностями менеджера контекста),
# которая может на вход принимать строки SQL запросов и возвращать данные в формате json.
# Класс должен иметь, как минимум, методы select и execute.
import json
import sqlite3 as sq


class SqLiteWrapper:
    def __init__(self, db_name):
        with sq.connect(db_name) as self.con:
            self.cur = self.con.cursor()

    def select(self, req):
        self.cur.execute(req)
        data = self.cur.fetchall()
        print(data)
        response = []
        for i in range(len(data)):
            object_map = {}
            for j in range(len(data[i])):
                key = self.cur.description[j][0]
                value = data[i][j]
                object_map[key] = value
            response.append(object_map)
        return json.dumps(response)

    def execute(self, req):
        self.cur.executescript(req)
        if 'CREATE' in req:
            return json.dumps({'table': 'created'})
        elif 'INSERT' in req:
            return json.dumps({'data': 'inserted'})
        elif 'DROP' in req:
            return json.dumps({'table': 'dropped'})


if __name__ == '__main__':
    my_connector = SqLiteWrapper('humans.db')
    print(my_connector.execute("""CREATE TABLE IF NOT EXISTS humans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )"""))
    print(my_connector.execute("INSERT INTO humans VALUES(1,'Mark',33)"))
    print(my_connector.execute("INSERT INTO humans VALUES(2,'Petr',29)"))
    print(my_connector.select("SELECT * FROM humans"))
    print(my_connector.execute("DROP TABLE humans"))
