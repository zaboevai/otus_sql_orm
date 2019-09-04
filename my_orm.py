import sqlite3

from models import News, User, Post


class DataBase:

    def __init__(self, data_base_path=None):

        self.data_base_path = data_base_path or './data_base.db'
        self.connect = sqlite3.connect(self.data_base_path)
        self.cursor = self.connect.cursor()
        self.tables = []
        self.query = None

    def init_data_base(self):
        """
        Initialize data base params and create tables
        :return:
        """
        self.connect.execute('PRAGMA foreign_keys = ON')
        self.tables.append(News())
        self.tables.append(User())
        self.tables.append(Post())

        for table in self.tables:
            try:
                self.create_table(table)
            except BaseException as exc:
                print(f'Таблица "{table.__table_name__}" уже существует или {exc}')

    def create_table(self, schema, recreate=False):
        """
        Create table or recreate table
        :param schema: table class
        :param recreate: True/False if needed to drop and create table
        :return:
        """
        if recreate:
            self.drop_table(schema)

        prepared_columns = schema.columns_to_insert
        sql = ",".join(prepared_columns)
        self.cursor.execute(f'CREATE TABLE {schema.__table_name__} ({sql})')
        print(f'Таблица {schema.__table_name__} успешно создана')

    def drop_table(self, schema):
        """
        Drop table
        :param schema: table class
        :return:
        """
        self.cursor.execute(f'DROP TABLE {schema.__table_name__}')
        print(f'Таблица {schema.__table_name__} удалена')

    def insert(self, rows):
        """
        :param rows: table instance or tuple of  tables instance
        :return: None
        """
        if not isinstance(rows, tuple):
            rows = (rows,)

        for row in rows:
            try:
                columns = []
                values = []
                for column in row.columns_names:
                    columns.append(column)
                    values.append(row.values[column])
                columns = ','.join(['?' for _ in columns])

                sql = f"INSERT INTO {row.__table_name__} VALUES ({columns})"
                self.cursor.execute(sql, values)
                print(f'Запись вставлена в {row.__table_name__}')
            except sqlite3.IntegrityError as exc:
                print(f'Запись уже существует или "{exc}"')
                continue

        self.connect.commit()

    def update(self, schema, set_param, where_param):
        """
        Update table values
        :param schema:
        :param set_param:
        :param where_param:
        :return:
        """
        sql = f"""
        UPDATE {schema.__table_name__} 
        SET {set_param[0]} = '{set_param[1]}' 
        WHERE {where_param[0]} = '{where_param[1]}'
        """
        self.cursor.execute(sql)
        self.connect.commit()
        print(f'Запись {where_param} обновлена на {set_param} из таблицы {schema.__table_name__}')

    def delete(self, schema, column):
        """
        Delete data from table
        :param schema:
        :param column:
        :return:
        """
        sql = f"DELETE FROM {schema.__table_name__} WHERE {column[0]} = '{column[1]}'"
        self.cursor.execute(sql)
        self.connect.commit()
        print(f'Запись {column} удалена из таблицы {schema.__table_name__}')

    def select(self, schema, query=None):
        """
        Select data from table
        :param schema:
        :param query:
        :return:
        """
        self.query = query or {1: 1}

        res = [f"{column}={value!r}" for column, value in self.query.items()]
        where = f"WHERE " + ' and '.join(map(str, res))
        sql = f"SELECT * FROM {schema.__table_name__}\n" + where

        join = ''  # f'join {} on {} \n'
        self.cursor.execute(sql)
        print(self.cursor.fetchall())
