# Implementare Meniu Interactiv

from Biblioteca import Biblioteca
from Carte import Carte
from Autor import Autor
from Utilizator import Utilizator


carte1 = Carte(1,"Baltagul", "Mihail Sadoveanu", "Romane", 1866)
carte2 = Carte(2,"1984", "George Orwell", "Romane", 1949)
carte3 = Carte(3,"Poezii", "Mihai Eminescu", "Poezii", 1934)

biblioteca = Biblioteca()
biblioteca.adauga_carte(carte1)
biblioteca.adauga_carte(carte2)
biblioteca.adauga_carte(carte3)
def meniuBiblioteca():

    while True:
        print("\n--- Meniu Biblioteca ---")
        print("1. Afiseaza carti disponibile")
        print("2. Adauga carte")
        print("3. Adauga utilizator")
        print("4. Imprumuta carte")
        print("5. Returneaza carte")
        print("6. Adauga rating la o carte")
        print("7. Cauta carti")
        print("8. Afiseaza total carti disponibile")
        print("9. Afiseaza total carti imprumutate")
        print("10. Afiseaza numarul total de carti al bibliotecii")
        print("11. Listeaza carti disponibile dintr-o categorie")
        print("12. Listeaza carti cu rating mai mare de 4")
        print("13. Sorteaza carti")
        print("14. Top 3 cele mai citite categorii")
        print("15. Iesire")

        optiune = input("Alege o optiune: ")

        if optiune == "1": # Afiseaza carti disponibile
            biblioteca.afiseaza_carti()


        elif optiune == "2": # Adauga Carte
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
                if carte.titlu.lower() == titlu_carte.lower():
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

        elif optiune == "6": # Adauga rating
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

        elif optiune == "7": # Cauta carti
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

        elif optiune == "13": # Sorteaza carti
            criteriu = input("Introduceti criteriul de sortare: ")
            carti_sortate = biblioteca.sortare_carti(criteriu)
            for carte in carti_sortate:
                print(carte)

        elif optiune == "14": # Top 3 cele mai citite categorii
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