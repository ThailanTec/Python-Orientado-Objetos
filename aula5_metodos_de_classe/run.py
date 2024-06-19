class MyClass:
    opa = "Opaio"
    def __init__(self, estado) -> None:
        self.estado = estado
    
    def print_Var(self):
        print(self.opa)

    @classmethod
    def altera(cls):
        cls.opa = "coisinha linda"
        

    
m = MyClass("Lala")
m.altera()
m.print_Var()


