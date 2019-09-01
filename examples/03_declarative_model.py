import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Post(Base):
    __tablename__ = 'posts'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    title = sqlalchemy.Column(sqlalchemy.String(16), nullable=False)
    text = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    is_publised = sqlalchemy.Column(sqlalchemy.Boolean, default=False)


if __name__ == '__main__':
    engine = sqlalchemy.create_engine('sqlite:///blog.db')
    Base.metadata.create_all(engine)

# Table First
# UML First
# Code First