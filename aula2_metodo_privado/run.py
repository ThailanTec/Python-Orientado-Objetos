class Pessoa:
    def __init__(self, altura, cpf) -> None:
        self.altura = altura
        self.__cpf = cpf
    
    def apresentar(self):
        print(f"Olá, meu nome é: Juluio, meu cpf é {self.cpf}")
    
    def __coletar_doc(self):
        print(f"documento coletado: {self.cpf}")


jorge = Pessoa("1.70", "126.224.974")

jorge._coletar_doc()