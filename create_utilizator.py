from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()
engine = create_engine('mysql+pymysql://root@127.0.0.1:3306/proiect_biblioteca', echo=True)

print(engine.connect())

class UtilizatorBaza(Base):
    __tablename__ = 'utilizatori'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nume = Column(String(50))
    carti_imprumutate = Column(String(50), default=0)

    def __repr__(self):
        return f'Utilizatorul {self.nume} cu id:{self.id} are cont in biblioteca.'

    def imprumuta_carte(self, carte, biblioteca):
        if biblioteca.imprumuta_carte(carte, self):
            if self.carti_imprumutate == '0':
                self.carti_imprumutate = str(carte.titlu) + ', '
            else:
                self.carti_imprumutate = self.carti_imprumutate + str(carte.titlu) + ', '
            print(f'{self.nume} a imprumutat {carte}')

    def returneaza_carte(self, carte, biblioteca):
        if biblioteca.returneaza_carte(carte, self):
            self.carti_imprumutate = self.carti_imprumutate.replace(carte.titlu, '')
            print(self.carti_imprumutate)
            print(f'{self.nume} a returnat "{carte.titlu}"')


print(Base.metadata.create_all(engine))
