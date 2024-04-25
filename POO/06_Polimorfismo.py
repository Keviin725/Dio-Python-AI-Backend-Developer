class Passaro:
    def voar(self):
        print("Voando")

class Pinguim(Passaro):
    def voar(self):
        print("Não pode voar")

class Pato(Passaro):
    def voar(self):
        print("Voando")
class Avestruz(Passaro):
    def voar(self):
        print("Não pode voar")

def plano_voo(obj):
    obj.voar()

p1 = Pinguim()
p2 = Pato()
p3 = Avestruz()

plano_voo(p1)
plano_voo(p2)
plano_voo(p3)