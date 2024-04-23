class Animal:
    def __init__(self, nome, numero_patas, cor, ambiente):
        self.nome = nome
        self.numero_patas = numero_patas
        self.cor = cor
        self.ambiente = ambiente

    def __str__(self):
        return f'{self.nome} {self.cor}'

    def falar(self):
        raise NotImplementedError("A subclasse deve implementar o método abstrato")

    def comer(self):
        print(f"{self.nome} está comendo")

    def andar(self):
        print(f"{self.nome} está andando")

class Mamifero(Animal):
    def __init__(self, nome, numero_patas, cor, ambiente, tipo_pelo):
        Animal.__init__(self, nome, numero_patas, cor, ambiente)
        self.tipo_pelo = tipo_pelo
    
    def falar(self):
        print(f"{self.nome} está fazendo barulho")
class Ave(Animal):
    def __init__(self, nome, numero_patas, cor, ambiente, tipo_pena):
        super().__init__(nome=nome, numero_patas=numero_patas, cor=cor, ambiente=ambiente)
        self.tipo_pena = tipo_pena

    def falar(self):
        print(f"{self.nome} está cantando")

    def voar(self):
        print(f"{self.nome} está voando")

class Gato(Mamifero):
    def __init__(self, nome, cor, ambiente, tipo_pelo):
        super().__init__(nome, 4, cor, ambiente, tipo_pelo)

    def falar(self):
        print(f"{self.nome} está miando")

class GatoVoador(Mamifero, Ave):
    def __init__(self, nome, cor, ambiente, tipo_pelo, tipo_pena):
        Mamifero.__init__(self, nome, 4, cor, ambiente, tipo_pelo)
        Ave.__init__(self, nome, 4, cor, ambiente, tipo_pena)

    def falar(self):
        print(f"{self.nome} está miando e cantando")
# Create instances of the classes
animal = Animal("Animal", 4, "Marrom", "Floresta")
mamifero = Mamifero("Mamífero", 4, "Preto", "Terra", "Curto")
ave = Ave("Ave", 2, "Azul", "Ar", "Macia")
gato = Gato("Gato", "Branco", "Casa", "Curto")
gato_voador = GatoVoador("Gato Voador", "Cinza", "Casa", "Curto", "Macia")

# Invoke the methods
animal.comer()
animal.andar()
mamifero.falar()
mamifero.falar()
ave.falar()
ave.voar()
gato.falar()
gato_voador.falar()
