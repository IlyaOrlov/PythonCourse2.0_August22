import cx_Oracle


host = '192.168.10.21'
username = 'USER'
password = '123456'
port = 1521
sid = 'mydb'
dbname = cx_Oracle.makedsn(host, port, sid=sid)
connection = cx_Oracle.connect(username, password, dbname)
