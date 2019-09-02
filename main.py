from models import News, Post, User
from my_orm import DataBase

db = DataBase()
db.init_data_base()
db.insert(News, ({'title': 'Заголовок 1', 'text': 'Новость 1'}, {'title': 'Заголовок 3', 'text': 'Новость 3'}))
db.insert(News, {'title': 'Заголовок 2', 'text': 'Новость 2'})
db.insert(News, {'title': 'Заголовок 3', 'text': 'Новость 3'})

db.select(News, )
db.select(News, {'title': 'Заголовок 4'})

db.insert(User, {'name': 'Admin'})

db.select(User, {'id': '1'})

db.insert(Post, {'user_id': '1', 'title': 'Заголовок 5', 'text': 'Новость 5'})
db.insert(Post, {'user_id': '2', 'title': 'Заголовок 6', 'text': 'Новость 6'})

db.select(Post, {'title': 'Заголовок 3'})

# db.drop_table(News)
