from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:///session.db')

# Проверить в нескольких потоках scope
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
session = Session()
session2 = Session()
# без scope
# session = session_factory()
# session2 = session_factory()
print(session is session2)