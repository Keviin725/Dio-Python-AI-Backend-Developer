# Definindo a classe Veiculo
class Veiculo:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def acelerar(self):
        print(f'{self.modelo} acelerando...')

    def frear(self):
        print(f'{self.modelo} freando...')

    def __str__(self):
        return f'{self.marca} {self.modelo} {self.ano} {self.cor}'

# Definindo a classe Moto que herda da classe Veiculo
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cor, cilindradas):
        super().__init__(marca, modelo, ano, cor)
        self.cilindradas = cilindradas

    def acelerar(self):
        print(f'{self.modelo} acelerando muito...')

    def empinar(self):
        print(f'{self.modelo} empinando...')

    def __str__(self):
        return f'{self.marca} {self.modelo} {self.ano} {self.cor} {self.cilindradas}cc'

# Definindo a classe Carro que herda da classe Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor, portas):
        super().__init__(marca, modelo, ano, cor)
        self.portas = portas

    def acelerar(self):
        print(f'{self.modelo} acelerando muito...')

    def abrir_porta(self):
        print(f'{self.modelo} abrindo a porta...')

    def __str__(self):
        return f'{self.marca} {self.modelo} {self.ano} {self.cor} {self.portas} portas'
    
# Criando uma instância da classe Moto
moto = Moto('Honda', 'CBR 1000RR', 2021, 'Vermelha', 1000)
print(moto)
moto.acelerar()
moto.empinar()

# Criando uma instância da classe Carro
carro = Carro('Chevrolet', 'Camaro', 2021, 'Amarelo', 2)
print(carro)
carro.acelerar()
carro.abrir_porta()