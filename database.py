from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeferredReflection, declarative_base
from sqlalchemy.orm import backref, relationship, scoped_session, sessionmaker

engine = create_engine("mysql+pymysql://root:0192837465@localhost/test")
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base(cls=DeferredReflection)

Base.query = db_session.query_property()
