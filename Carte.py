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