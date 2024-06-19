class MyClass:
    opa = "Opaio"
    def __init__(self, estado) -> None:
        self.estado = estado
    
m = MyClass("Lala")

print(MyClass.opa)