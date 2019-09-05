from models import News, Post, User
from my_orm import DataBase

db = DataBase()
db.init_data_base()

db.insert(User(name='Admin'))
rows = (News(title='Заголовок 1', text='Новость 1'),
        News(title='Заголовок 2', text='Новость 2'),
        Post(user=1, title='Заголовок 3', text='Новость 3'))

db.insert(rows=rows)

rows = News(title='Заголовок 3', text='Новость 3')
db.insert(rows=rows)

db.select(schema=News(), )
db.select(schema=News(), where_param={'title': 'Заголовок 2', 'text': 'Новость 2'})

db.insert(Post(user=2, title='Заголовок 3', text='Новость 3'))

db.select(schema=Post(), where_param={'title': 'Заголовок 3'})

db.select(schema=Post(), join_schema=User(), where_param={'title': 'Заголовок 3'})

db.delete(schema=News(), where_param={'title': 'Заголовок 2'})
db.update(schema=Post(), set_param={'text': 'Новость 1321233'}, where_param={'title': 'Заголовок 3'})

db.drop_table(News())
