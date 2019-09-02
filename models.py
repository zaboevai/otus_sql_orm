class Base:
    __table_name__ = ''

    id = ('INTEGER', 'PRIMARY KEY', 'AUTOINCREMENT')

    def __init__(self, **kwargs):
        self._param = kwargs

    @property
    def columns(self):
        field_names = [f'{k if k != "key" else ""} {" ".join(v)}' for k, v in self.__class__.__dict__.items()
                       if not k.startswith('__')]
        return field_names

    @property
    def param(self):
        return self._param


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


row = News(id='1', title='123', text='asd')

print(row.columns)
print(row.param)
