from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base, engine


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
