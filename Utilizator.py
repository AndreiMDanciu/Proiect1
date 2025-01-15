from Persoana import Persoana

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