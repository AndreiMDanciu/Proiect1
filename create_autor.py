from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('mysql+pymysql://root@127.0.0.1:3306/proiect_biblioteca', echo=True)

print(engine.connect())

class Autor(Base):
    __tablename__ = 'autori'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nume = Column(String(50))
    carti_scrise = Column(String(50))

print(Base.metadata.create_all(engine))