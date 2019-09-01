import sqlalchemy
from sqlalchemy.orm import mapper

engine = sqlalchemy.create_engine('sqlite:///blog.db')
metadata = sqlalchemy.MetaData()

post_table = sqlalchemy.Table('posts', metadata,
                              sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
                              sqlalchemy.Column('user_id', sqlalchemy.Integer, nullable=False),
                              sqlalchemy.Column('title', sqlalchemy.String(16), nullable=False),
                              sqlalchemy.Column('text', sqlalchemy.Text, nullable=False),
                              sqlalchemy.Column('is_publised', sqlalchemy.Boolean, default=False),
                              )


class Post:
    def __init__(self, user_id, title, text, is_published):
        self.user_id = user_id
        self.title = title
        self.text = text
        self.is_published = is_published


mapper(Post, post_table)

if __name__ == '__main__':
    metadata.create_all(engine)
