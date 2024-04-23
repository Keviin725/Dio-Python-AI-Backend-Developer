class Cachorro:
    def __init__(self, nome, idade, cor, acordado=True):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print('Au au')

    def __del__(self):
        print(f'{self.nome} foi deletado')

def criar_cachorro():
    c = Cachorro('Totó', 10, 'Marrom', True)
    c.latir()
    print(c.nome)
    print(c.idade)

    return c

c = criar_cachorro()
c.latir()
#print(c.nome)
#print(c.idade)

del c