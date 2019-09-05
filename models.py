class Base:
    __table_name__ = ''

    id = ('INTEGER', 'PRIMARY KEY', 'AUTOINCREMENT')

    def __init__(self, **kwargs):
        self._values = kwargs
        if 'id' not in kwargs:
            self._values['id'] = None

    @property
    def columns_to_insert(self):
        field_names = [f'{k} {" ".join(v)}' for k, v in self.__class__.__dict__.items()
                       if not k.startswith('__')]
        return field_names

    @property
    def columns_names(self):
        field_names = [f'{k if k != "key" else ""}' for k in self.__class__.__dict__.keys()
                       if not k.startswith('__')]
        return field_names

    @property
    def values(self):
        return self._values

    def get_foreign_key(self):
        field_names = [f'{column}' for column, value in self.__class__.__dict__.items()
                       if not column.startswith('__') and 'REFERENCES' in value]
        return field_names

    def __str__(self):
        return self.__table_name__


class News(Base):
    __table_name__ = 'news'
    id = Base.id
    title = ('char(256)', 'not null')
    text = ('char(256)', 'not null')


class User(Base):
    __table_name__ = 'user'
    id = Base.id
    name = ('char(256)', 'not null')


class Post(Base):
    __table_name__ = 'post'

    id = Base.id
    user = ('INTEGER', 'REFERENCES', f'{User()}(id)')
    title = ('char(256)', 'not null')
    text = ('char(256)', 'not null')
