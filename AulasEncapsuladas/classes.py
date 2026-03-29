class Animal:
    def __init__(self,nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self,alimento):
        return f'O {self.nome} está comendo {alimento}'

    def executar(self,hum):
        return self.comendo(hum)

leao = Animal('Leão')
print(leao.nome)
print(leao.comendo('Jacaré'))

print(leao.executar('rafael'))