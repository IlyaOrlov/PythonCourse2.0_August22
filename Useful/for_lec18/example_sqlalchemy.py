import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm.session import close_all_sessions

Base = declarative_base()

# Создаем класс, отображающий таблицу
class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    position = Column(String, ForeignKey('position_salary.position'),
                      nullable=False)
    bonus = Column(Integer, default=0)
    login = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    def __repr__(self):
        return "<Employee(id={id}, name='{name}'," \
               " position='{pos}', bonus={bon}," \
               " login='{log}', password='{pwd}')>".\
            format(id=self.id, name=self.name,
                   pos=self.position, bon=self.bonus,
                   log=self.login, pwd=self.password)

class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    def __repr__(self):
        return "<Project(id={id}, name='{name}')>".format(id=self.id,
                                                          name=self.name)

class PositionSalary(Base):
    __tablename__ = 'position_salary'
    position = Column(String, primary_key=True)
    salary = Column(Integer, nullable=False)
    def __repr__(self):
        return "<PositionSalary(position='{pos}', salary={sal})>".format(
            pos=self.position, sal=self.salary)

class EmployeeProject(Base):
    __tablename__ = 'employee_project'
    employee_id = Column(Integer, ForeignKey('employee.id'), primary_key=True)
    project_id = Column(Integer, ForeignKey('project.id'), primary_key=True)
    def __repr__(self):
        return "<EmployeeProject(employee_id={e_id}, project_id={p_id})>".\
            format(e_id=self.employee_id, p_id=self.project_id)


class DBClient:

    def __init__(self, dbtype='sqlite', dbname='/example.db',
                 username=None, password=None):
        self._engine = self._get_engine(dbtype, dbname, username, password)

    def __enter__(self):
        self._session = sessionmaker(bind=self._engine)()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        close_all_sessions()

    @staticmethod
    def _get_engine(dbtype, dbname, username=None, password=None):
        if username:
            if password:
                login = '{u}:{p}'.format(u=username, p=password)
            else:
                login = username
            dbstr = '{l}@{db}'.format(l=login, db=dbname)
        else:
            dbstr = dbname

        # Создаем базу данных
        # Либо без файла (в оперативной памяти)
        # Либо с файлом, указывая относительный путь к нему: engine = create_engine('sqlite:///mybase.db')
        # Либо абсолютный путь: engine = create_engine(r'sqlite:///C:\Users\User\Desktop\mybase.db')
        engine = create_engine('{}:///{}'.format(dbtype, dbstr))
        return engine

    def create_schema(self):
        # Создаем схему
        Base.metadata.create_all(self._engine)

    def delete_schema(self):
        # Удаляем схему
        Base.metadata.drop_all(self._engine)

    def insert_position(self, position, salary):
        self._session.add(PositionSalary(position=position, salary=salary))
        self._session.commit()

    def insert_project(self, name):
        p = Project(name=name)
        self._session.add(p)
        self._session.commit()
        return p.id

    def insert_employee(self, name, position, bonus, login, password):
        e = Employee(name=name, position=position, bonus=bonus,
                     login=login, password=password)
        self._session.add(e)
        self._session.commit()
        return e.id

    def add_employee_to_project(self, employee_id, project_id):
        self._session.add(EmployeeProject(employee_id=employee_id,
                                          project_id=project_id))
        self._session.commit()


    def add_new_employee_to_project(self, name, position, bonus, login, password, project_id):
        e = Employee(name=name, position=position, bonus=bonus,
                     login=login, password=password)
        self._session.add(e)
        self._session.commit()
        self._session.add(EmployeeProject(employee_id=e.id,
                                          project_id=project_id))
        self._session.commit()


    # Проверка наличия пользователя в базе данных
    # с указанным логином/паролем
    def authentication(self, login, password):
        try:
            res = self._session.query(Employee.id, Employee.name,
                                      Employee.position, EmployeeProject.project_id).\
                join(EmployeeProject, EmployeeProject.employee_id == Employee.id). \
                filter(and_(Employee.login == login,
                            Employee.password == password)).\
            one()
            return res
        except MultipleResultsFound:
            print("Multiple Results Found")
        except NoResultFound:
            print("No Result Found")
        return None

    # Проверка наличия указанного сотрудника в указанном проекте
    def is_employee_in_project(self, employee_id, project_id):
        try:
            res = self._session.query(EmployeeProject.project_id).\
                filter(and_(EmployeeProject.employee_id == employee_id,
                            EmployeeProject.project_id == project_id)).\
                one()
            return True
        except MultipleResultsFound:
            print("Multiple Results Found")
        except NoResultFound:
            print("No Result Found")
        return None


    # Вывод информации для сотрудника
    # Соединяем таблицы Employees, PositionSalary
    def show_employee_info(self, employee_id):
        res = self._session.query(Employee.id, Employee.name,
                                  (PositionSalary.salary +
                                  Employee.bonus).label("Pay")).\
            filter(and_(Employee.position == PositionSalary.position,
                        Employee.id == employee_id)).\
            all()
        print("Информация для сотрудника:")
        for row in res:
            print(row)
        return res

    # Вывод информации для менеджера проекта
    # Соединяем таблицы Employees, PositionSalary, EmployeeProject
    def show_manager_info(self, project_id):
        res = self._session.query(Employee.id, Employee.name,
                                  (PositionSalary.salary +
                                   Employee.bonus).label("Pay")). \
            filter(and_(Employee.position == PositionSalary.position,
                        Employee.id == EmployeeProject.employee_id,
                        EmployeeProject.project_id == project_id)). \
            all()
        print("Информация для менеджера:")
        for row in res:
            print(row)
        return res

    # Изменение премии сотрудника
    def update_employee_bonus(self, employee_id, new_bonus):
        e = self._session.query(Employee).get(employee_id)
        if e:
            e.bonus = new_bonus
            self._session.add(e)
            self._session.commit()

    # Удаление сотрудника из проекта (но не из базы данных)
    def delete_employee_from_project(self, employee_id, project_id):
        ep = self._session.query(EmployeeProject).get((employee_id, project_id))
        if ep:
            self._session.delete(ep)
            self._session.commit()


    def show_all(self):
        print(self._session.query(PositionSalary).all())
        print(self._session.query(Project).all())
        print(self._session.query(Employee).all())
        print(self._session.query(EmployeeProject).all())


if __name__ == "__main__":
    db_type = "sqlite"
    db_name = "example.db"
    db_exists = os.path.exists(db_name)

    if not db_exists:
        with DBClient(db_type, db_name) as dbc:
            dbc.create_schema()

            dbc.insert_position("инженер", 50000)
            dbc.insert_position("старший инженер", 51000)
            dbc.insert_position("менеджер проекта", 100000)

            pid = dbc.insert_project("Важный")
            eid = dbc.insert_employee("Иванов И.И.", "инженер", 30000,
                                      "ivanovi", "ivanov123")
            dbc.add_employee_to_project(eid, pid)

            eid = dbc.insert_employee("Петров П.П.", "старший инженер", 50000,
                                      "petrovp", "p1e2t3")
            dbc.add_employee_to_project(eid, pid)

            pid = dbc.insert_project("Срочный")
            dbc.add_employee_to_project(eid, pid)

            eid = dbc.insert_employee("Сидоров С.С.", "менеджер проекта", 30000,
                                "sidorovs", "zayka88")
            dbc.add_employee_to_project(eid, pid)


    login = input("Логин: ")
    pwd = input("Пароль: ")
    with DBClient(db_type, db_name) as dbc:
        #dbc.show_all()
        res = dbc.authentication(login, pwd)
        if res:
            user = res._asdict()
            print("Здравствуйте, {}".format(user['name']))
            if user['position'] == "менеджер проекта":
                dbc.show_manager_info(user['project_id'])

                id_upd = int(input("Изменение премии. ID сотрудника (0 - отмена): "))
                if id_upd:
                    if (id_upd != user['id'] and
                            dbc.is_employee_in_project(id_upd, user['project_id'])):
                        new_bonus = input("Новая премия: ")
                        dbc.update_employee_bonus(id_upd, new_bonus)
                        print("Результат:")
                        dbc.show_manager_info(user['project_id'])
                    else:
                        print("Невозможно изменить премию для данного сотрудника")

                id_del = int(input("Удаление сотрудника. ID сотрудника (0 - отмена): "))
                if id_del:
                    if id_del != user['id']:
                        dbc.delete_employee_from_project(id_del, user['project_id'])
                        print("Результат:")
                        dbc.show_manager_info(user['project_id'])
                    else:
                        print("Невозможно удалить данного сотрудника из проекта")
            else:
                dbc.show_employee_info(user['id'])
        else:
            print("Доступ запрещен")
