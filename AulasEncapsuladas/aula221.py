class Pessoa:
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(self.nome,self.sobrenome,self.__class__.__name__)

class Cliente(Pessoa):
    ...

class Aluno(Pessoa):
    ...

c1 = Cliente('Josekson','Silva')
c1.falar_nome_classe()
c2 = Aluno('Victor','Luna')
c2.falar_nome_classe()

help(Cliente)