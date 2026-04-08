class PetRepository:
    def __init__(self):
        self.pets = []

    def adicionar(self, pet):
        self.pets.append(pet)

    def buscar_por_nome(self, nome):
        for p in self.pets:
            if p.nome == nome:
                return p
        return None

    def listar(self):
        return self.pets