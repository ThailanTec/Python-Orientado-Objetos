### O que é Orientação a Objetos?

Orientação a objetos é um paradigma aplicado na programação que consiste na interação entre diversas unidades chamadas de objetos. 

A arquitetetura de software e a programação orientada a objetos estão intimamente relacionadas, pois a programação orientada a objetos é uma das abordagens mais comuns para desenvolver sistemas dentro de uma arquitetura de software. 

***Importante***

Quando se trata de arquietura de software, a programação orientada a objetos é frequentemente usada para implementar conceitos arquiteturais, como MVC, camadas de aplicação, componetização, entre outros. 

### Sobre UML

É uma linguagem de anotação (um jeito de escrever, ilustrar, comunicar) para uso em projetos de sistemas. 

***Importante***
Fornecer a arquitetos de sistemas e engenheiros ferramentas de analises, design e implementação para sistemas baseados em software, bem como para a modelagem de processos de negćios e similares. 

## Conceitos Básicos (Código)

## Classes

São um conjunto/contexto em si, considerando atributos e metodos. 

**Atributos**: caracteristicas. (Cor, Tamanho, altura, dados)

**Metodos**: ações. (Correr, download, listar, deletar)

Atraves de uma classe, nos instanciamos um objeto, como no exemplo abaixo:

```python
class Zoid:
    def metodo1(self):
        print("hello wordi")

minha = Zoid()

minha.metodo1()

```

A classe Zoid, está instanciada no objeto minha. Uma classe por si só, não realiza ação. Mas o objeto sim. 

### Metodo construtor

O metodo construtor é o primeiro a iniciar na aplicação. Para declarar um construtor em Python, podemos fazer da seguinte forma no inicio da classe:

```python
class Zoid:
    def __init__(self): # metodo construtor 
        nome: str

```

Também, temos os metodos que podem utilizar dessas classes privada, sendo assim mais fácil de manusear durante todo esse código. Como podemos ver no exemplo abaixo:

```python
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
```

### Metodos privados

Para escrever metodos nos quais não podem ou não devem ser acessados em outros locais dos códigos, utilizamos o “__” assim, o código fica privado. 

```python
class Pessoa:
    def __init__(self, altura, cpf) -> None:
        self.altura = altura
        self.cpf = cpf
    
    def apresentar(self):
        print(f"Olá, meu nome é: Juluio, meu cpf é {self.cpf}")
    
    def __coletar_doc(self):
        print(f"documento coletado: {self.cpf}")

jorge = Pessoa("1.70", "126.224.974")

jorge._coletar_doc()
```

O metodo coletar_doc não pode ser acessado, nossa saida é:

```python
➜  aula2_metodo_privado git:(master) ✗ py [run.py](http://run.py/)
Traceback (most recent call last):
File "/home/thailandev/Área de Trabalho/python-estudos/Python-Orientado-Objetos/aula2_metodo_privado/run.py", line 15, in <module>
jorge._coletar_doc()
AttributeError: 'Pessoa' object has no attribute '_coletar_doc'
```

O mesmo funciona para nossos atributos, caso não desejamos que um atributo seja acessado por outras classes, podemos privar o seu acesso: 

```python
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
```

Como no caso do **CPF** na função acima. 

Podemos acessar um atributo privado, mas não devemos pois vai causar um grande problema no código. Assim, deixando a mesma privada dentro da sua propia classe. 

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/ea9dccf6-7ab8-443c-bff2-9d4deaf3ce72/b2224e1c-6392-496e-8d3d-3621c02805df/Untitled.png)

No diagrama UML tudo o que está com o ‘+’ mostra que pode ser acessado por outra classe, mas o que está com sinal de ‘-’ não pode ser acessado por outra classe e deve ficar indisponivel. 

## Getters/Setters & Encapsulamentos

Quando pegamos um metodo que tem um valor privado e alteramos o seu valor, nós quebramos um dos valores principais da OO que é o emcapsulamento. Exemplo de quebra de emcapsulamento:

**ERRADO!!!**

```python
class MinhaClass:
    def __init__(self) -> None:
        self.__valor = None

my_class = MinhaClass()

my_class.__valor = 554

print(my_class.__valor)
```

Para não ferir o emcapsulamento precisamos criar então, metodos para suprir a alteração desses dados. Os metodos são do “tipo” getter (pegar) e setter (setar) informações ou recolher informações dos metodos que são privados e desejamos alterar, pois dessa forma conseguimos ter um total controle do que vai ser alterado quando o dado novo for enviado. 

**CERTO!!!**

```python
class MinhaClass:
    def __init__(self) -> None:
        self.__valor = None
    
    def setter(self, valor:int) -> None:
        self.__valor = valor
    
    def getter(self)-> int:
        return self.__valor

my_class = MinhaClass()
my_class.setter(3)

print(my_class.getter())

```

Dessa forma, mantemos a aplicação com qualidade e com uma segurança maior, podendo ter regras para o retorno e também para que os dados dos usuários tenham uma segurança maior também no momento da sua exibição. 

**Extra:**

Podemos utilizar dentro da nossa função um decator, que tem o papel de transformar nossa função como se ele fosse um atributo da classe. Exemplo: 

```python
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

```

Assim, podemos ter os retornos que desejamos na nossa classe. 

### Váriaveis de Classes

Quando criamos uma váriavel dentro de uma classe: 

```python
class MyClass:
    opa = "Opaio"
    def __init__(self, estado) -> None:
        self.estado = estado
    
m = MyClass("Lala")

print(MyClass.opa)
```

O valor dela é replicado por todo o código da classe, assim, caso seja alterado posteriormente em toda a classe esse valor será alterado. Lembrando que o variavel está sendo declarada fora do construtor. Assim, sendo de acesso a qualquer um que queira utilizar nossa classe. 

### Metodos de Classes

Para que possamos acessar o contexto geral de uma classe, utilizamos o **@classmethod,** 

assim vamos conseguir por exemplo alterar o comportamento geral de uma *váriavel de classe.* 

```python
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

```

### Exercicio de Metodos de Classes

Nesse exercicio, conseguimos modificar o valor da taxa e conseguimos mudar para produtos especificos.

```python
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

```