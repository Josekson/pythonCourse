class Pessoa:

    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def metodo_classe(cls):
        print('Hey')

    @classmethod
    def criar_idade_50(cls,nome):
        return cls(nome,50)

    @classmethod
    def criar_sem_nome(cls,idade):
        return cls('Anônimo',idade)

p1 = Pessoa('Joao',27)
Pessoa.metodo_classe()
p2 = Pessoa.criar_idade_50('Maria')
p3 = Pessoa.criar_sem_nome(100)
print(p3.idade)