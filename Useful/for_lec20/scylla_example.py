from cassandra.cluster import Cluster


def insert_users(id, username, fullname, regdate, status):
    session.execute(
        "INSERT INTO users (id, username, fullname, regdate, status) VALUES (%s, %s, %s, %s, %s)",
        (id, username, fullname, regdate, status)
    )

def select_users(id=None):
    if id is None:
        res = session.execute("SELECT * FROM users")
    else:
        res = session.execute("SELECT * FROM users WHERE id = %s", (id,))
    if res:
        res = [item for item in res]
    return res

def update_user_status(new_status, id=None):
    if id is None:
        session.execute("UPDATE users SET status = %s", (new_status))
    else:
        session.execute("UPDATE users SET status = %s WHERE id = %s", (new_status, id))

def delete_users(id=None):
    if id is None:
        res = session.execute("DELETE FROM users")
    else:
        res = session.execute("DELETE FROM users WHERE id = %s", (id,))


cluster = Cluster(['127.0.0.1'])
session = cluster.connect('example')

insert_users(1, 'ivanovi', 'Иван Иванов', '2020-01-01', 'Available')
insert_users(2, 'petrovp', 'Петр Петров', '2020-02-02', 'Busy')
insert_users(3, 'orlovi', 'Илья Орлов', '2020-03-03', 'Available')

print(select_users())
print(select_users(1))
update_user_status('Busy', 1)
print(select_users(1))
delete_users(3)
print(select_users())
