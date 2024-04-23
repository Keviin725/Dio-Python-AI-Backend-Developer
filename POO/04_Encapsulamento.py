class Conta:
    def __init__(self, saldo, nr_agencia):
        self.__saldo = saldo
        self.nr_agencia = nr_agencia

    def deposito(self, valor):
        self._saldo += valor
    
    def levantamento(self, valor):
        self.__saldo -= valor
    
    def mostrar_saldo(self):
        return self.__saldo
conta = Conta(1000, "0001")
conta.deposito(500)
conta.levantamento(750)
print(conta.mostrar_saldo())
#print(conta.__saldo) # AttributeError: 'Conta' object has no attribute '__saldo'