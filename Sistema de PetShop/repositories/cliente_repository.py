class ClienteRepository:
    def __init__(self):
        self.clientes = []

    def adicionar(self, cliente):
        self.clientes.append(cliente)

    def buscar_por_documento(self, documento):
        for c in self.clientes:
            if c.documento == documento:
                return c
        return None

    def listar(self):
        return self.clientes