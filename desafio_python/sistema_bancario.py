from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)
 

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, endereco, data_nascimento):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero, cliente):
        self.__numero = numero
        self.__agencia = "0001"
        self.__saldo = 0
        self.__cliente = cliente
        self.__historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    @property
    def saldo(self):
        return self.__saldo
    @property
    def numero(self):
        return self.__numero
    @property
    def agencia(self):
        return self.__agencia
    @property
    def cliente(self):
        return self.__cliente
    @property
    def historico(self):
        return self.__historico
    
    def levantar(self, valor):
        saldo = self.saldo()
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            raise ValueError("Saldo insuficiente")
        elif valor > 0:
            self.__saldo -= valor
            print("\n@@@ Levantamento efetuado com sucesso @@@")
            return True
        else:
            print("\n@@@ Valor inválido @@@")
            return False
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print("\n@@@ Depósito efetuado com sucesso @@@")
        else:
            print("\n@@@ Valor inválido @@@")
            return False
        return True
        
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def levantar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes
                            if transacao["tipo"] == Saque.__name__])
        
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n@@@ Limite excedido @@@")
        elif excedeu_saques:
            print("\n@@@ Limite de saques excedido @@@")
        else:
            super().levantar(valor)
            return True
        return False
    
    def __str__(self):
        return f"Conta Corrente {self.numero} - Agência {self.agencia} - Titular {self.cliente.nome}"
    

class Historico:
    def __init__(self):
        self.transacoes = []
    
    def transacoes(self):
        return self.__transacoes

    def registrar_transacao(self, transacao):
        self.__transacoes.append({
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor
        })

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self.__valor = valor
    
    @property
    def valor(self):
        return self.__valor
    

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.registrar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self.__valor = valor
    
    @property
    def valor(self):
        return self.__valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.registrar_transacao(self)
    
    
