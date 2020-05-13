from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine
from sqlalchemy.ext.declarative import DeferredReflection, declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# engine = create_engine("mysql+pymysql://root:0192837465@localhost/test")
engine = create_engine("sqlite:///testdb.db", echo=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base(cls=DeferredReflection)

Base.query = db_session.query_property()

meta = MetaData()

user = Table(
    "user",
    meta,
    Column("iduser", Integer, primary_key=True),
    Column("name", String),
    Column("lastname", String),
)

user = Table(
    "person",
    meta,
    Column("idperson", Integer, primary_key=True),
    Column("name", String),
)

meta.create_all(engine)
