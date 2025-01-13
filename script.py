# PROIECT 1
###############

from functools import reduce

def afisare(func):
    def wrapper(*args, **kwargs):
        print(f"Se apeleaza functia: {func.__name__}")
        rezultat = func(*args, **kwargs)
        return rezultat
    return wrapper

class Persoana:
    def __init__(self, id_persoana, nume):
        self.id = id_persoana
        self.nume = nume

    def __str__(self):
        return f"Persoana {self.nume} - id: {self.id}"

class Utilizator(Persoana):
    def __init__(self, id_persoana, nume):
        super().__init__(id_persoana, nume)
        self.carti_imprumutate = []
        self.istoric_imprumuturi = set()

    def imprumuta_carte(self, carte, biblioteca):
        if biblioteca.imprumuta_carte(carte, self):
            self.carti_imprumutate.append(carte)
            self.istoric_imprumuturi.add(carte.titlu)
            print(f'{self.nume} a imprumutat {carte}')

    def returneaza_carte(self, carte, biblioteca):
        if carte in self.carti_imprumutate:
            biblioteca.returneaza_carte(carte, self)
            self.carti_imprumutate.remove(carte)
            print(f'{self.nume} a returnat "{carte.titlu}"')

    def statistici_personale(self):
        print(f'{self.nume} a imprumutat in total {len(self.istoric_imprumuturi)} carti.')
        for carte in self.carti_imprumutate:
            print(f"Carte imprumutata {carte.titlu}")

class Autor:
    def __init__(self, id_autor, nume):
        self.id_autor = id_autor
        self.nume = nume
        self.carti_scrise = []

    def adauga_carte(self, carte):
        if carte in self.carti_scrise:
            print(f"Cartea {carte.titlu} este deja adaugata pentru autorul {self.nume}.")
        else:
            self.carti_scrise.append(carte)
            print(f'Cartea "{carte.titlu}" de {carte.autor} a fost adaugata.')

class Carte:
    def __init__(self, id_carte, titlu, autor, categorie, an_publicatie):
        self.id_carte = id_carte
        self.titlu = titlu
        self.autor = autor
        self.categorie = categorie
        self.an_publicatie = an_publicatie
        self.disponibila = True
        self.rating = []
        self.rating_total = 0

    def adauga_rating(self, nota):
        if 1 <= nota <= 5:
            self.rating.append(nota)
        else:
            print("Introduceti un rating valid(1-5).")
        self.rating_total = sum(self.rating) / len(self.rating)
        return self.rating_total

    def __str__(self):
        return f"{carte.id_carte} - '{carte.titlu}' de {carte.autor}, an publicatie: {carte.an_publicatie}, rating: {carte.rating_total}"

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
        return reduce(lambda acc, carte: acc + (1 if carte.disponibila else 0), self.lista_carti, 0)

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
    def categorii_populare(self):
        categorii = {}





# Implementare Meniu Interactiv


carte1 = Carte(1,"Crima si Pedeapsa", "Dostoievski", "Romane", 1866)
carte2 = Carte(2,"1984", "George Orwell", "Romane", 1949)
carte3 = Carte(3,"Poezii", "Mihai Eminescu", "Poezii", 1934)

biblioteca = Biblioteca()
biblioteca.adauga_carte(carte1)
biblioteca.adauga_carte(carte2)
biblioteca.adauga_carte(carte3)

while True:
    print("\n--- Meniu Biblioteca ---")
    print("1. Afiseaza carti disponibile") # MERGE
    print("2. Adauga carte") # MERGE
    print("3. Adauga utilizator") # MERGE
    print("4. Imprumuta carte") # MERGE
    print("5. Returneaza carte") # !!!!!!!!!!!!!
    print("6. Adauga rating la o carte") # MERGE
    print("7. Cauta carti") # MERGE
    print("8. Afiseaza total carti disponibile") # MERGE
    print("9. Afiseaza total carti imprumutate") # MERGE
    print("10. Afiseaza numarul total de carti al bibliotecii") # MERGE
    print("11. Listeaza carti disponibile dintr-o categorie") # MERGE
    print("12. Listeaza carti cu rating mai mare de 4") # MERGE
    print("13. Sorteaza carti") # MERGE
    print("14. Top 3 cele mai citite categorii") # MERGE
    print("15. Iesire")

    optiune = input("Alege o optiune: ")

    if optiune == "1":
        biblioteca.afiseaza_carti()


    elif optiune == "2":
        id_carte = int(input("ID Carte: "))
        titlu = input("Titlu: ")
        nume_autor = input("Nume autor: ")
        categorie = input("Categorie: ")
        an_publicatie = int(input("An publicatie: "))

        autor = Autor(id_carte, nume_autor)
        carte = Carte(id_carte, titlu, nume_autor, categorie, an_publicatie)
        biblioteca.adauga_carte(carte)

    elif optiune == "3": # Adauga utilizator
        id_utilizator = int(input("ID Utilizator: "))
        nume = input("Nume: ")
        utilizator = Utilizator(id_utilizator, nume)
        biblioteca.adauga_utilizator(utilizator)

    elif optiune == "4": # Imprumuta carte
        id_utilizator = int(input("ID Utilizator: "))
        titlu_carte = input("Titlu carte: ")
        utilizator = biblioteca.utilizatori.get(id_utilizator)

        for carte in biblioteca.lista_carti:
            if carte.titlu == titlu_carte:
                carte_de_imprumutat = carte

        if utilizator and carte_de_imprumutat:
            utilizator.imprumuta_carte(carte_de_imprumutat, biblioteca)
        else:
            print("Utilizator sau carte inexistenta!")

    elif optiune == "5":  # Returnează carte
        id_utilizator = int(input("ID Utilizator: "))
        titlu_carte = input("Titlu carte: ")
        utilizator = biblioteca.utilizatori.get(id_utilizator)

        for carte in utilizator.carti_imprumutate:
            if carte.titlu.lower() == titlu_carte.lower():
                carte_de_returnat = carte

        if utilizator and carte_de_returnat:
            utilizator.returneaza_carte(carte_de_returnat, biblioteca)
        else:
            print("Utilizator sau carte inexistenta!")

    elif optiune == "6":
        titlu_carte = input("Introduceti titlul cartii: ")
        rating = int(input("Introduceti rating(1-5): "))
        if rating < 1 or rating > 5:
            print("Rating invalid! Introduceti un rating valid (1-5)!")
            continue

        carte_cu_rating = None
        for carte in biblioteca.lista_carti:
            if carte.titlu.lower() == titlu_carte.lower():
                carte_cu_rating = carte
                break

        if carte_cu_rating:
            carte_cu_rating.adauga_rating(rating)
            print(f"Rating-ul {rating} a fost adaugat pentru cartea {carte_cu_rating.titlu} de {carte_cu_rating.autor}")
            print(f"Ratingul cartii '{carte_cu_rating.titlu}' este {carte_cu_rating.rating_total}")
        else:
            print("Cartea nu a fost gasita sau rating invalid!")

    elif optiune == "7":
        criteriu = input("Introduceti criteriul(autor, categorie, an, rating): ")
        valoare = input("Introduceti valoarea(nume, categorie, an, rating): ")
        rezultat = biblioteca.cauta_carte(criteriu, valoare)
        if rezultat:
            for carte in rezultat:
                print(carte)
        else:
            print("Nu s-au gasit carti pentru criteriul sau valoarea introduse!")

    elif optiune == "8": # Total carti disponibile
        total_carti_disponibile = biblioteca.carti_disponibile()
        if total_carti_disponibile:
            print(f"Biblioteca are momentan {total_carti_disponibile} carti disponibile!")
        else:
            print("Nu sunt carti disponibile in biblioteca momentan!")

    elif optiune == "9": # Total carti imprumutate
        total_carti_imprumutate = biblioteca.carti_imprumutate()
        if total_carti_imprumutate:
             print(f"Biblioteca are momentan {total_carti_imprumutate} carti imprumutate!")
        else:
            print("Nu sunt carti imprumutate momentan!")

    elif optiune == "10": # Total carti biblioteca
        total_carti = biblioteca.total_carti()
        if total_carti:
            print(f"Biblioteca are in total {total_carti} carti!")
        else:
            print("Nu sunt carti in biblioteca! Adaugati carti!")

    elif optiune == "11": # Afisare carti disponibile dintr-o categorie
        categorie = input("Introduceti categoria dorita: ")
        carti = biblioteca.carti_disponibile_categorie(categorie)
        if carti:
            print(f"Pentru categoria {categorie} sunt disponibile urmatoarele carti: ")
            for carte in carti:
                print(f"- '{carte.titlu}' de {carte.autor} publicata in anul {carte.an_publicatie}")
        else:
            print(f"Nu sunt carti disponibile pentru categoria {categorie}!")

    elif optiune == "12": #Listare carti cu rating > 4
        carti_populare = biblioteca.carti_rating_mai_mare_4()
        if not carti_populare:
            print("Nicio carte cu rating mai mare de 4!")
        for carte in carti_populare:
            print(f"Carte {carte.titlu} are rating-ul {carte.rating_total}")

    elif optiune == "13":
        criteriu = input("Introduceti criteriul de sortare: ")
        carti_sortate = biblioteca.sortare_carti(criteriu)
        for carte in carti_sortate:
            print(carte)

    elif optiune == "14":
        top_3 = biblioteca.top_3_categorii()
        print("Cele mai citite 3 categorii: ")
        for categorie, frecvente in top_3:
            print(f"{categorie}: {frecvente} imprumuturi.")
    # #
    elif optiune == "15":
        print("La revedere!")
        break
    else:
        print("Optiune invalida!")
