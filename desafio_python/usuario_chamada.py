class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano

    def fazer_chamada(self, destinatario, duracao):
        custo = self.__plano.custo_chamada(duracao)
        if self.__plano.verificar_saldo() >= custo:
            self.__plano.deduzir_saldo(custo)
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${self.__plano.verificar_saldo():.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."

class Plano:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    def verificar_saldo(self):
        return self.__saldo

    def custo_chamada(self, duracao):
        return duracao * 0.10

    def deduzir_saldo(self, valor):
        self.__saldo -= valor

class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))

nome = input()
numero = input()
saldo_inicial = float(input())
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))