from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('mysql+pymysql://root@127.0.0.1:3306/proiect_biblioteca', echo=True)

print(engine.connect())

class CarteBaza(Base):
    __tablename__ = 'carti'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titlu = Column(String(50))
    autor = Column(String(50))
    categorie = Column(String(40))
    an_publicatie = Column(String(40))
    rating = Column(Float, default=0)
    recenzii = Column(Integer, default=0)
    disponibilitate = Column(Boolean, default=True)

    def __repr__(self):
        return f'Cartea (id={self.id}, titlu="{self.titlu}" de {self.autor}, an_publicatie: {self.an_publicatie}, rating: {self.rating})'

    def adauga_rating(self, nota):
        if 1 <= nota <= 5:
            self.rating = (self.rating * self.recenzii) + nota
            self.recenzii += 1
        else:
            print("Introduceti un rating valid(1-5).")
        self.rating = self.rating / self.recenzii

print(Base.metadata.create_all(engine))

# Session = sessionmaker()
# Session.configure(bind=engine)
# session = Session()
# session.commit()