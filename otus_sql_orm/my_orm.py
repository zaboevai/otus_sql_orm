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

    @staticmethod
    def prepare_columns(columns):
        prepared_column = []
        for name, value in columns.items():
            if name == 'mro' or name.startswith('__'):
                continue
            column = f'{name} {" ".join(value)}'
            prepared_column.append(column)

        return prepared_column

    def init_data_base(self):
        self.tables.append(News)
        self.tables.append(User)
        self.tables.append(Post)

        for table in self.tables:
            try:
                self.create_table(table)
            except sqlite3.OperationalError:
                print(f'Таблица "{table.__table_name__}" уже существует')

    def get_table_info(self, schema):
        self.table_info = schema.__class__.__dict__
        # self.table_name = self.table_info['__table_name__']

    def create_table(self, schema, recreate=False):

        if recreate:
            self.drop_table(schema)

        self.get_table_info(schema)
        prepared_columns = self.prepare_columns(self.table_info)
        sql = ",".join(prepared_columns)
        self.cursor.execute(f'CREATE TABLE {schema.table_name} ({sql})')
        print(f'Таблица {schema.table_name} успешно создана')

    def drop_table(self, schema):
        self.cursor.execute(f'DROP TABLE {schema.__table_name__}')
        print(f'Таблица {schema.__table_name__} удалена')

    def insert(self, schema, values):
        try:
            self.cursor.execute(f"INSERT INTO {schema.__table_name__} VALUES (?, ?, ?)", values)
            self.connect.commit()
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

    def select(self, schema, column, value):
        sql = f"SELECT * FROM {schema.__table_name__} WHERE {column}='{value}'"
        self.cursor.execute(sql)
        print(self.cursor.fetchall())
