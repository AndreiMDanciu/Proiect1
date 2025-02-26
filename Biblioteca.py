from sqlalchemy import Boolean
from functools import reduce

from create_carte import *
from create_utilizator import *
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

def afisare(func):
    def wrapper(*args, **kwargs):
        print(f"Se apeleaza functia: {func.__name__}")
        rezultat = func(*args, **kwargs)
        return rezultat
    return wrapper

class Biblioteca:
    def __init__(self):
        self.lista_carti = []
        self.utilizatori = {}

    def adauga_carte(self, carte): ### cu SQL merge
        status = True
        for item in self.lista_carti:
            if carte.titlu.lower() == item.titlu.lower():
                status = False
        if status:
            self.lista_carti.append(carte)
            carte_noua = CarteBaza(titlu=carte.titlu, autor=carte.autor, categorie=carte.categorie, an_publicatie=carte.an_publicatie)
            session.add(carte_noua)
            session.commit()
            print(f'Cartea "{carte.titlu}" de {carte.autor} a fost adaugata.')
        else:
            print("Carte deja existenta!")


    def adauga_utilizator(self, utilizator):  ### cu SQL merge
        self.utilizatori[utilizator.id] = utilizator
        utilizator_nou = UtilizatorBaza(nume=utilizator.nume)
        session.add(utilizator_nou)
        session.commit()
        print(f"Utilizatorul '{utilizator.nume}' a fost adaugat in biblioteca.")

    @afisare
    def imprumuta_carte(self, carte, utilizator):  ##
        carti = session.query(CarteBaza).all()
        print(carte)
        if carte.disponibilitate:
            print(carte.disponibilitate)
            carte.disponibilitate = False
            session.commit()
            return True
        else:
            print(f'Cartea {carte.titlu} nu este disponibila!')

    @afisare
    def returneaza_carte(self, carte, utilizator):
        carti = session.query(CarteBaza).all()
        print(carte.disponibilitate)
        if not carte.disponibilitate:
            carte.disponibilitate = True
            session.commit()
            return True
        else:
            print(f'Cartea {carte.titlu} nu a fost imprumutata!')


    #Cautare dupa autor, categorie, an sau rating
    def cauta_carte(self, criteriu, valoare):
        carti = session.query(CarteBaza).all()
        if criteriu.lower() == "autor":
            return [carte for carte in carti if carte.autor.lower() == valoare.lower()]
        elif criteriu.lower() == "categorie":
            return [carte for carte in carti if carte.categorie.lower() == valoare.lower()]
        elif criteriu.lower() == "an":
            return [carte for carte in carti if carte.an_publicatie == int(valoare)]
        elif criteriu.lower() == "rating":
            return [carte for carte in carti if carte.rating_total >= int(valoare)]
        else:
            return("Optiune invalida. Va rugam selectati un criteriu")


    def cauta_carte_dupa_id(self, id_carte):
        return (carte for carte in self.lista_carti if carte.id_carte == id_carte)


    def afiseaza_carti(self): ### cu SQL merge
        carti_disponibile = []
        carti = session.query(CarteBaza).all()
        for carte in carti:
            if carte.disponibilitate:
                carti_disponibile.append(carte)
        if carti_disponibile:
            print(f"Cartile disponibile in biblioteca -> {len(carti_disponibile)}:")
            for carte in carti_disponibile:
                print(f"{carte.id} - '{carte.titlu}' de {carte.autor}")

    #Numarul total de carti disponibile
    def carti_disponibile(self):
        carti = session.query(CarteBaza).all()
        return reduce(lambda res, carte: res + (1 if carte.disponibilitate else 0), carti, 0)

    #Cele mai populare categorii


    #Cartile disponibile dintr-o anumita categorie
    def carti_disponibile_categorie(self, categorie): ### cu SQL merge
        carti = session.query(CarteBaza).all()
        return list(filter(lambda carte: carte.disponibilitate and carte.categorie.lower() == categorie.lower(), carti))

    #Carti cu rating > 4
    def carti_rating_mai_mare_4(self):
        carti = session.query(CarteBaza).all()
        carti =  list(filter(lambda carte: carte.rating > 4, carti))
        return carti

    #Sortare carti dupa an, categorie sau rating
    def sortare_carti(self, criteriu): ### cu SQL merge
        carti = session.query(CarteBaza).all()
        if criteriu == "an":
            return sorted(carti, key=lambda carte: carte.an_publicatie)
        elif criteriu == "categorie":
            return sorted(carti, key=lambda carte: carte.categorie)
        elif criteriu == "rating":
            return sorted(carti, key=lambda carte: carte.rating, reverse=True)
        else:
            return carti

    #Statistici si Rapoarte
    #Total carti
    def total_carti(self):
        carti = session.query(CarteBaza).all()
        return reduce(lambda res, carte: res + 1, carti, 0)

    #Numar de carti imprumutate
    def carti_imprumutate(self):
        carti = session.query(CarteBaza).all()
        return reduce(lambda res, carte: res + (0 if carte.disponibilitate else 1), carti, 0)

    #Cele mai citite 3 categorii
    def top_3_categorii(self):
        categorii = {}
        # carti = session.query(CarteBaza).all()

        for utilizator in self.utilizatori.values():
            for titlu_carte in utilizator.istoric_imprumuturi:
                for carte in self.lista_carti:
                    if carte.titlu == titlu_carte:
                        if carte.categorie in categorii:
                            categorii[carte.categorie] += 1
                        else:
                            categorii[carte.categorie] = 1
        top_3_categorii = sorted(categorii.items(), key=lambda x: x[1], reverse = True)[:3]
        return top_3_categorii

    #Cele mai populare 3 categorii
    # def categorii_populare(self):
    #     categorii = {}



