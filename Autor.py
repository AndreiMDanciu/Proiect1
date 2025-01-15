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