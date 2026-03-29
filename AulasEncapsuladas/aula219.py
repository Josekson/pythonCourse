class Carro:
    def __init__(self,nome):
        self.nome = nome
        self.motor_nome = None
        self.fabricante_nome = None

    @property
    def motor(self):
        return self.motor_nome
    
    @motor.setter
    def motor(self,nome):
        self.motor_nome = nome


    @property
    def fabricante(self):
        return self.fabricante_nome
    
    @fabricante.setter
    def fabricante(self,nome):
        self.fabricante_nome = nome


class Motor:
    def __init__(self, nome):
        self.nome = nome
        #self.carros = []
    
'''    def inserir_carro_composicao(self,nome):
        self.carros.append(Carro(nome))'''

class Fabricante:
    def __init__(self,nome):
        self.nome = nome
        #self.carros = []
    
'''    def inserir_carro_composicao(self,nome):
        self.carros.append(Carro(nome))'''


c1 = Carro('Celta')
m1 = Motor('XJ001')
f1 = Fabricante('Volkswagem')

c1.motor = m1
c1.fabricante = f1
print(c1.nome,c1.motor.nome,c1.fabricante.nome)


c2 = Carro('Uno')
f2 = Fabricante('Fiat')
c2.motor = m1
c2.fabricante = f2
print(c2.nome,c2.motor.nome,c2.fabricante.nome)

c3 = Carro('Focus')
m3 = Motor('ABC 1.0')
c3.motor = m3
c3.fabricante = f1

print(c3.nome,c3.motor.nome,c3.fabricante.nome)