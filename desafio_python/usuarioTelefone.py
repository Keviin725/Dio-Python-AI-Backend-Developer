'''
Desafio
Vamos criar uma classe chamada UsuarioTelefone para representar um usuário de telefone. Você pode definir um método especial e depois aplicar conceitos de encapsulamento nos atributos dentro da classe. Lembre-se que, cada usuário terá um nome, um número de telefone e um plano associado, neste desafio, simulamos três planos, sendo: Plano Essencial Fibra, Plano Prata Fibra e Plano Premium Fibra.

Entrada
Nome do usuário, número de telefone e plano.

Saída
Mensagem indicando que o usuário foi criado com sucesso.
'''

class UsuarioTelefone:
    def __init__(self, nome, telefone, plano):
        self.__nome = nome
        self.__telefone = telefone
        self.__plano = plano

    def __str__(self):
        return f"Usuário {self.__nome} criado com sucesso."


nome = input()
telefone = input()
plano = input()

usuario = UsuarioTelefone(nome, telefone, plano)


print(usuario)