class Base:
    __table_name__ = ''

    id = ('INTEGER', 'PRIMARY KEY', 'AUTOINCREMENT')

    def __init__(self, **kwargs):
        self._values = kwargs
        if 'id' not in kwargs:
            self._values['id'] = None

    @property
    def columns_to_insert(self):
        field_names = [f'{k if k != "key" else ""} {" ".join(v)}' for k, v in self.__class__.__dict__.items()
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
    user_id = ('INTEGER', 'REFERENCES user(id)')
    title = ('char(256)', 'not null')
    text = ('char(256)', 'not null')
