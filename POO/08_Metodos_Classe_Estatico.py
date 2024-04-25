class Pessoa:
    # Atributo de classe
    populacao = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        # Incrementa a população sempre que uma nova pessoa é criada
        Pessoa.populacao += 1

    # Método de classe
    @classmethod
    def get_populacao(cls):
        # Retorna o valor do atributo de classe 'populacao'
        return cls.populacao

    # Método estático
    @staticmethod
    def is_adulto(idade):
        # Retorna True se a idade for maior ou igual a 18, caso contrário, retorna False
        return idade >= 18

p1 = Pessoa('João', 20)
p2 = Pessoa('Maria', 15)

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)

# Usando o método de classe
print("População:", Pessoa.get_populacao())

# Usando o método estático
print("João é adulto?", Pessoa.is_adulto(p1.idade))
print("Maria é adulto?", Pessoa.is_adulto(p2.idade))