class People:
    def __init__(self, idade: int, altura: float) -> None:
        self.idade = idade
        self.altura = altura

    def correr(self):
        if self.idade >= 18 and self.altura > 1.75:
            print("Pode correr na maratona")
        else:
            print("Não vai da não")

    def comer(self):
        if self.altura > 18:
            print("Você tem de comer 3x ao dia")
        

pessoa = People(18, 1.76)

pessoa.comer()
pessoa.correr()