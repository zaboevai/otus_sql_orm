import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///blog.db')
metadata = sqlalchemy.MetaData()

post_table = sqlalchemy.Table('posts', metadata,
                              sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
                              sqlalchemy.Column('user_id', sqlalchemy.Integer, nullable=False),
                              sqlalchemy.Column('title', sqlalchemy.String(16), nullable=False),
                              sqlalchemy.Column('text', sqlalchemy.Text, nullable=False),
                              sqlalchemy.Column('is_publised', sqlalchemy.Boolean, default=False),
                              )

if __name__ == '__main__':
    metadata.create_all(engine)
