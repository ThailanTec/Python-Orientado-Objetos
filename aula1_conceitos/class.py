class Zoid:
    def __init__(self, estado, memoria): # metodo construtor 
        self.nome: str
        self.in_memory: memoria
        self.estado: estado

    def metodo1(self):
        self.nome = "Você"
        

    def meto3(self):
        self.metodo1()
        print(self.estado)


minha = Zoid("Ola", 'mundo')

minha.metodo1()
minha.meto3()



        