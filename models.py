class Base:
    id = ('INTEGER', 'PRIMARY KEY', 'AUTOINCREMENT')
    __table_name__ = ''

    def get_columns(self):
        field_names = [f'{k if k != "key" else ""} {" ".join(v)}' for k, v in self.__class__.__dict__.items() if
                       not k.startswith('__')]
        return field_names


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
    user_id = ('INTEGER', 'not null', 'REFERENCES user(id)')
    title = ('char(256)', 'not null')
    text = ('char(256)', 'not null')
