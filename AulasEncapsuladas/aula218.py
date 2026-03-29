class Cliente:
    def __init__(self,nome):
        self.nome = nome
        self.enderecos = []
    
    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua,numero))

    def listar_enderecos(self):
        print()
        for endereco in self.enderecos:
            print(endereco.rua,endereco.numero)
        print()

class Endereco:
    def __init__(self,rua, numero):
        self.rua = rua
        self.numero = numero

c1 = Cliente('josekson')
c1.inserir_endereco('Rua itaji',452)
c1.inserir_endereco('Rua b',457)
c1.listar_enderecos()
print(c1.enderecos[1].numero)