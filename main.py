from models import News, Post, User
from my_orm import DataBase

db = DataBase()
db.init_data_base()

db.insert(User(name='Admin'))

rows = (News(title='Заголовок 1', text='Новость 1'),
        News(title='Заголовок 2', text='Новость 2'),
        Post(user_id=1, title='Заголовок 3', text='Новость 3'))

db.insert(rows)

rows = News(title='Заголовок 3', text='Новость 3')
db.insert(rows)

db.select(News, )
db.select(News, {'title': 'Заголовок 2', 'text': 'Новость 2'})

db.insert(Post(user_id=2, title='Заголовок 3', text='Новость 3'))

db.select(Post, {'title': 'Заголовок 3'})
db.delete(News, ('title', 'Заголовок 2'))
db.update(Post, ('text', 'Новость 1321233'), ('title', 'Заголовок 3'))

# db.drop_table(News)
