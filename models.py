from sqlalchemy import *
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship, scoped_session, sessionmaker

from database import Base, engine, db_session


class PersonModel(Base):
    __tablename__ = "person"
    idperson = Column(Integer, primary_key=True)
    name = Column(String)


class UserModel(Base):
    __tablename__ = "user"
    iduser = Column(Integer, primary_key=True)
    name = Column(String)
    idperson = Column(ForeignKey("person.idperson"))
    person = relationship("PersonModel")


Base.prepare(engine)
