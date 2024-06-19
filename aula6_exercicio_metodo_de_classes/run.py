class Loja:
    taxa = 1.40

    def __init__(self, valor) -> None:
        self.valor_product = valor

    def consulta_valor(self):
       valor_p = self.valor_product * self.taxa
       print(f"valor do produto {valor_p}")
    
    @classmethod
    def editar_taxa_product(cls, n_taxa: float):
        cls.taxa = n_taxa


l = Loja(40.53)
l.editar_taxa_product(2.60)
l.consulta_valor()

b = Loja(80.32)
b.editar_taxa_product(1.2)
b.consulta_valor()
