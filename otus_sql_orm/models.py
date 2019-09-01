
class News:
    __table_name__ = 'news'

    columns = [
        {'id': ('int', 'primary key')},
        {'title': ('char(256)', 'null')},
        {'text': ('char(256)', 'null')},
    ]


class User:
    __table_name__ = 'user'

    columns = [
        {'id': ('int', 'primary key')},
        {'name': ('char(256)', 'null')}
    ]


class Post:
    __table_name__ = 'post'

    columns = [
        {'id': ('int', 'primary key')},
        {'title': ('char(256)', 'null')},
        {'text': ('char(256)', 'null')},
    ]