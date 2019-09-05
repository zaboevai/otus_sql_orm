import sqlite3

from models import News, User, Post


class DataBase:

    def __init__(self, data_base_path=None):

        self.data_base_path = data_base_path or './data_base.db'
        self.connect = sqlite3.connect(self.data_base_path)
        self.cursor = self.connect.cursor()
        self.tables = []

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
        self.cursor.execute(f'CREATE TABLE {schema} ({sql})')
        print(f'Таблица {schema} успешно создана')

    def drop_table(self, schema):
        """
        Drop table
        :param schema: table class
        :return:
        """
        self.cursor.execute(f'DROP TABLE {schema}')
        print(f'Таблица {schema} удалена')

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

                sql = f"INSERT INTO {row} VALUES ({columns})"
                self.cursor.execute(sql, values)
                print(f'Запись вставлена в {row}')
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
        sql_set = [f"{column}={value!r}" for column, value in set_param.items()]
        sql_set = f"\n SET " + ', '.join(map(str, sql_set))

        sql_where = [f"{column}={value!r}" for column, value in where_param.items()]
        sql_where = f"\n WHERE " + ' and '.join(map(str, sql_where))

        sql = f'UPDATE {schema}' + sql_set + sql_where

        self.cursor.execute(sql)
        self.connect.commit()
        print(f'Запись {where_param} обновлена на {set_param} из таблицы {schema}')

    def delete(self, schema, where_param):
        """
        Delete data from table
        :param schema:
        :param where_param:
        :return:
        """
        sql_query = [f"{column}={value!r}" for column, value in where_param.items()]
        sql_where = f"WHERE " + ' and '.join(map(str, sql_query))
        sql = f"DELETE FROM {schema} " + sql_where
        self.cursor.execute(sql)
        self.connect.commit()
        print(f'Запись {where_param} удалена из таблицы {schema}')

    def select(self, schema, join_schema=None, where_param=None):
        """
        Select data from table
        :param schema:
        :param join_schema:
        :param where_param:
        :return:
        """
        where_param = where_param or {1: 1}

        sql_where = [f"{column}={value!r}" for column, value in where_param.items()]
        sql_where = f"\n WHERE " + ' and '.join(map(str, sql_where))
        sql_join = ''

        if join_schema:
            fk = schema.get_foreign_key()
            sql_join = f'\n JOIN {join_schema} on {schema}.{fk[0]}={join_schema}.id'

        sql = f"SELECT * FROM {schema}\n" + sql_join + sql_where

        self.cursor.execute(sql)
        print(self.cursor.fetchall())
