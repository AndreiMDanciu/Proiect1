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

    def adauga_carte(self, carte):
        self.lista_carti.append(carte)
        print(f'Cartea "{carte.titlu}" de {carte.autor} a fost adaugata.')

    def adauga_utilizator(self, utilizator):
        self.utilizatori[utilizator.id] = utilizator
        print(f"Utilizatorul '{utilizator.nume}' a fost adaugat in biblioteca.")

    @afisare
    def imprumuta_carte(self, carte, utilizator):
        if carte in self.lista_carti and carte.disponibila:
            carte.disponibila = False
            return True
        else:
            print(f'Cartea {carte.titlu} nu este disponibila!')
    @afisare
    def returneaza_carte(self, carte, utilizator):
        if carte in self.lista_carti and not carte.disponibila:
            carte.disponibila = True
            return True
        else:
            print(f'Cartea {carte.titlu} nu a fost imprumutata!')


    #Cautare dupa autor, categorie, an sau rating
    def cauta_carte(self, criteriu, valoare):
        if criteriu.lower() == "autor":
            return [carte for carte in self.lista_carti if carte.autor.lower() == valoare.lower()]
        elif criteriu.lower() == "categorie":
            return [carte for carte in self.lista_carti if carte.categorie.lower() == valoare.lower()]
        elif criteriu.lower() == "an":
            return [carte for carte in self.lista_carti if carte.an_publicatie == int(valoare)]
        elif criteriu.lower() == "rating":
            return [carte for carte in self.lista_carti if carte.rating_total >= int(valoare)]
        else:
            return("Optiune invalida. Va rugam selectati un criteriu")


    def cauta_carte_dupa_id(self, id_carte):
        return (carte for carte in self.lista_carti if carte.id_carte == id_carte)


    def afiseaza_carti(self):
        carti_disponibile = []
        for carte in self.lista_carti:
            if carte.disponibila:
                carti_disponibile.append(carte)
        if carti_disponibile:
            print(f"Cartile disponibile in biblioteca -> {len(carti_disponibile)}:")
            for carte in carti_disponibile:
                print(f"{carte.id_carte} - '{carte.titlu}' de {carte.autor}")

    #Numarul total de carti disponibile
    def carti_disponibile(self):
        return reduce(lambda res, carte: res + (1 if carte.disponibila else 0), self.lista_carti, 0)

    #Cele mai populare categorii


    #Cartile disponibile dintr-o anumita categorie
    def carti_disponibile_categorie(self, categorie):
        return list(filter(lambda carte: carte.disponibila and carte.categorie.lower() == categorie.lower(), self.lista_carti))

    #Carti cu rating > 4
    def carti_rating_mai_mare_4(self):
        carti =  list(filter(lambda carte: carte.rating_total > 4, self.lista_carti))
        return carti

    #Sortare carti dupa an, categorie sau rating
    def sortare_carti(self, criteriu):
        if criteriu == "an":
            return sorted(self.lista_carti, key=lambda carte: carte.an_publicatie)
        elif criteriu == "categorie":
            return sorted(self.lista_carti, key=lambda carte: carte.categorie)
        elif criteriu == "rating":
            return sorted(self.lista_carti, key=lambda carte: carte.rating, reverse=True)
        else:
            return self.lista_carti

    #Statistici si Rapoarte
    #Total carti
    def total_carti(self):
        return reduce(lambda res, carte: res + 1, self.lista_carti, 0)

    #Numar de carti imprumutate
    def carti_imprumutate(self):
        return reduce(lambda res, carte: res + (0 if carte.disponibila else 1), self.lista_carti, 0)

    #Cele mai citite 3 categorii
    def top_3_categorii(self):
        categorii = {}

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



