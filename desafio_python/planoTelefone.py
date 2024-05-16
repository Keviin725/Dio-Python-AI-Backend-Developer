class PlanoTelefone:
    def __init__(self, nome_plano, saldo_inicial):
        self.__nome_plano = nome_plano
        self.__saldo_inicial = saldo_inicial

    @property
    def nome_plano(self):
        return self.__nome_plano

    @property
    def saldo_inicial(self):
        return self.__saldo_inicial

    def verificar_saldo(self):
        return self.__saldo_inicial

    def mensagem_personalizada(self):
        if self.__saldo_inicial < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self.__saldo_inicial >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

class UsuarioTelefone:
    def __init__(self, nome_usuario, plano_usuario):
        self.__nome_usuario = nome_usuario
        self.__plano_usuario = plano_usuario

    @property
    def nome_usuario(self):
        return self.__nome_usuario

    @property
    def plano_usuario(self):
        return self.__plano_usuario

    def verificar_saldo(self):
        saldo = self.__plano_usuario.verificar_saldo()
        mensagem = self.__plano_usuario.mensagem_personalizada()
        return saldo, mensagem

nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, plano_usuario)

saldo_usuario, mensagem_usuario = usuario.verificar_saldo()
print(mensagem_usuario)