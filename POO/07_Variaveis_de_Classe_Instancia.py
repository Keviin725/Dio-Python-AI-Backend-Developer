class Estudante:
    escola = 'ISUTC'

    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
    
    def __str__(self) -> str:
        return f'Nome: {self.nome}, Idade: {self.idade}, Matricula: {self.matricula}, Escola: {self.escola}'

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno1 = Estudante('João', 20, 1234)
aluno2 = Estudante('Maria', 21, 1235)
aluno3 = Estudante('Pedro', 22, 1236)

mostrar_valores(aluno1, aluno2, aluno3)
Estudante.escola = "ISUTC - Instituto Superior de Transportes e Comunicações"
aluno1.matricula = 3
mostrar_valores(aluno1, aluno2, aluno3)