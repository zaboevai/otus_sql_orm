import sqlite3

from models import News, User, Post


class DataBase:

    def __init__(self, data_base_path=None):

        self.data_base_path = data_base_path or './data_base.db'
        self.connect = sqlite3.connect(self.data_base_path)
        self.cursor = self.connect.cursor()
        self.tables = []

    @staticmethod
    def prepare_columns(columns):
        prepared_column = []
        for column in columns:
            for name, value in column.items():
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

    def create_table(self, schema, recreate=False):
        if recreate:
            self.drop_table(schema)

        prepared_columns = self.prepare_columns(schema.columns)
        sql = ",".join(prepared_columns)
        self.cursor.execute(f'CREATE TABLE {schema.__table_name__} ({sql})')
        print(f'Таблица {schema.__table_name__} успешно создана')

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


db = DataBase()
db.init_data_base()
db.insert(News, (1, 'заголовок', 'текст'))
db.select(News, 'title', 'заголовок')
db.drop_table(News)
