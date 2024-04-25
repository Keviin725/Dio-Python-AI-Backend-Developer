from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    def marca(self):
        return "Samsung"

class ControleTV(ControleRemoto):
    def ligar(self):
        print('TV ligada')
    
    def desligar(self):
        print('TV desligada')

    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ar condicionado ligado')
    
    def desligar(self):
      print('Ar condicionado desligado')
    @property
    def marca(self):
        return "HP"
controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()

print(controle.marca)