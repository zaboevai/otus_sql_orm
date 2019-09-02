import sqlite3

from models import News, User, Post


class DataBase:

    def __init__(self, data_base_path=None):

        self.data_base_path = data_base_path or './data_base.db'
        self.connect = sqlite3.connect(self.data_base_path)
        self.cursor = self.connect.cursor()
        self.tables = []
        self.table_info = {}
        self.table_name = []
        self.query = None

    @staticmethod
    def prepare_columns(columns):
        prepared_column = []
        for name, value in columns.items():
            if name.startswith('__'):
                continue
            column = f'{name} {" ".join(value)}'
            prepared_column.append(column)

        return prepared_column

    def init_data_base(self):
        self.tables.append(News())
        self.tables.append(User())
        self.tables.append(Post())

        for table in self.tables:
            try:
                self.create_table(table)
            except sqlite3.OperationalError:
                print(f'Таблица "{table.__table_name__}" уже существует')

    def create_table(self, schema, recreate=False):

        if recreate:
            self.drop_table(schema)

        prepared_columns = schema.get_columns()
        sql = ",".join(prepared_columns)
        self.cursor.execute(f'CREATE TABLE {schema.__table_name__} ({sql})')
        print(f'Таблица {schema.__table_name__} успешно создана')

    def drop_table(self, schema):
        self.cursor.execute(f'DROP TABLE {schema.__table_name__}')
        print(f'Таблица {schema.__table_name__} удалена')

    def insert(self, schema, insert_values):
        try:
            id_table = {'id': None}
            values = insert_values

            if isinstance(values, dict):
                values = (values,)

            for value in values:
                prepared_values = {**id_table, **value}
                columns = ','.join(['?' for _ in range(len(prepared_values))])
                sql = f"INSERT INTO {schema.__table_name__} VALUES ({columns})"
                self.cursor.execute(sql, list(prepared_values.values()))

            self.connect.commit()
            print(f'Запись вставлена в {schema.__table_name__}')
        except sqlite3.IntegrityError:
            print('Запись уже существует')

    def update(self, schema, column, update_to):
        sql = f"""
        UPDATE {schema.__table_name__} 
        SET artist = '{update_to}' 
        WHERE artist = '{column}'
        """
        self.cursor.execute(sql)
        self.connect.commit()

    def delete(self, schema, column):
        sql = f"DELETE FROM {schema.__table_name__} WHERE artist = '{column}'"
        self.cursor.execute(sql)
        self.connect.commit()

    def select(self, schema, query=None):
        self.query = query or {1: 1}
        for k, v in self.query.items():
            sql = f"SELECT * FROM {schema.__table_name__} WHERE {k}={v!r}"
            self.cursor.execute(sql)
            print(self.cursor.fetchall())
