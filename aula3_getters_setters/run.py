class MinhaClass:
    def __init__(self) -> None:
        self.__valor = None
    
    def setter(self, valor:int) -> None:
        self.__valor = valor
    
    @property
    def getter(self)-> int:
        return self.__valor

my_class = MinhaClass()
my_class.setter(3)

print(my_class.getter)

