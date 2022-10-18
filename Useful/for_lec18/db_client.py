import logging
import csv
import cx_Oracle
import sqlite3


DB_CODE = 'cp1251'


def OutputTypeHandler(cursor, name, defaultType, size, precision, scale):
    if defaultType == cx_Oracle.CLOB:
        return cursor.var(cx_Oracle.LONG_STRING, arraysize=cursor.arraysize)
    if defaultType == cx_Oracle.BLOB:
        return cursor.var(cx_Oracle.LONG_BINARY, arraysize=cursor.arraysize)


class DBClient(object):

    def __init__(self, dbtype='sqlite', dbname='tmp.db',
                 username=None, password=None):
        self.dbtype = dbtype
        self.conn = self.connect(dbtype, dbname, username, password)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()
        
    
    @staticmethod
    def connect(dbtype, dbname, username=None, password=None):
        connection = None
        try:
            logging.debug('Create connection to db: dbtype={}, dbname={}'.format(dbtype, dbname))
            if dbtype == 'sqlite':
                connection = sqlite3.connect(dbname)
                connection.row_factory = sqlite3.Row
            elif dbtype == 'oracle':
                connection = cx_Oracle.connect(username, password, dbname)
                connection.outputtypehandler = OutputTypeHandler
        except Exception as err:
            logging.critical('Error: cannot connect to db. {}'.format(err))
            raise err
        return connection

    @staticmethod
    def show_multi_data(headline, rows, csvfilename=None):
        if csvfilename:
            with open(csvfilename, 'wb') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=headline)
                writer.writeheader()
                for r in rows:
                    # d = {k: v if isinstance(v, bytes) else v for k, v in dict(r).items()}
                    # writer.writerow(d)
                    writer.writerow(dict(r))
        else:
            logging.info(headline)
            for r in rows:
                logging.info('    {},'.format([x.decode(DB_CODE) if isinstance(x, bytes) else x for x in r]))

    def get_student_info(self):
        cur = self.conn.cursor()
        cur.execute('SELECT s.*, o.DESCRIPTION, o.INSERTED, os.STATUS_NAME '
                    'FROM edu_student s, edu_object o, edu_object_status os '
                    'WHERE s.OBJECT_ID = o.OBJECT_ID AND o.OBJECT_STATUS_ID = os.OBJECT_STATUS_ID')
        col_names = [each[0] for each in cur.description]
        cur.rowfactory = lambda *args: dict(zip([d[0] for d in cur.description], args))
        return col_names, cur.fetchall()

    def get_contract_info(self):
        cur = self.conn.cursor()
        cur.execute('SELECT co.CONTRACT_NUMBER, co.COST, co.BEGIN_DATE, co.END_DATE, '
                    'co.CREATION_DATE, co.CUSTOMER, '
                    'o2.OBJECT_NAME, o.DESCRIPTION, o.INSERTED, os.STATUS_NAME, '
                    's.LAST_NAME, s.FIRST_NAME, s.SECOND_NAME '
                    'FROM edu_contract co, edu_object o, edu_object o2, edu_student s, edu_object_status os '
                    'WHERE o.OBJECT_ID = co.OBJECT_ID AND o2.OBJECT_ID = co.COURSE_ID AND os.OBJECT_STATUS_ID = o.OBJECT_STATUS_ID '
                    'AND s.OBJECT_ID = co.STUDENT_ID')
        col_names = [each[0] for each in cur.description]
        cur.rowfactory = lambda *args: dict(zip([d[0] for d in cur.description], args))
        return col_names, cur.fetchall()

    def export_data_to_csv(self):
        col_names, rows = self.get_student_info()
        self.show_multi_data(col_names, rows, 'students.csv')
        col_names, rows = self.get_contract_info()
        self.show_multi_data(col_names, rows, 'contract.csv')
        # self.show_multi_data(col_names, rows)


