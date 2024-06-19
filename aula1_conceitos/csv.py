class CsvHandler:
    def __init__(self, directory) -> None:
        self.dir = directory

    def insert(self,data):
        print(f"To botando {data}, em {self.dir}")
    
    def ler(self):
        print(f"lendo os dados em{self.dir}")




csv = CsvHandler('./.csv')

csv.ler()
csv.insert("data")
