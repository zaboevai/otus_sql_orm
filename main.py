from models import News, Post
from my_orm import DataBase

db = DataBase()
db.init_data_base()
db.insert(News, {'title': 'Заголовок 1', 'text': 'Новость 1'})
db.insert(News, {'title': 'Заголовок 2', 'text': 'Новость 2'})
db.insert(News, {'title': 'Заголовок 3', 'text': 'Новость 3'})
db.select(News, {})
db.select(News, {'title': 'Заголовок 2;'})

db.insert(Post, {'title': 'Заголовок 3', 'text': 'Новость 3'})
# db.drop_table(News)

# db = DataBase()
n = News().get_columns()
p = Post().get_columns()
