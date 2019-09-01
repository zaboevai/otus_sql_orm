import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), nullable=False)
    title = sqlalchemy.Column(sqlalchemy.String(16), nullable=False)
    text = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    is_publised = sqlalchemy.Column(sqlalchemy.Boolean, default=False)

    user = relationship("User", back_populates="posts")


class User(Base):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    username = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)

    posts = relationship("Post", back_populates="user")


if __name__ == '__main__':
    engine = sqlalchemy.create_engine('sqlite:///blog.db')
    Base.metadata.create_all(engine)

