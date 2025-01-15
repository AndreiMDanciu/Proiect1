class Persoana:
    def __init__(self, id_persoana, nume):
        self.id = id_persoana
        self.nume = nume

    def __str__(self):
        return f"Persoana {self.nume} - id: {self.id}"