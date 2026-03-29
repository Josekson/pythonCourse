class Pessoa:

    ano_atual = 2025

    atributo = 'valor'
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 100

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


print(Pessoa.ano_atual)
p1 = Pessoa('Josekson',27) 
p2 = Pessoa('Helena',12)
p1.nome = 'jabil'
print(p1.nome)
print(p1.get_ano_nascimento()) 
print(p2.get_ano_nascimento())

dados = {'nome': 'jabil FDP!', 'idade': 27}
px = Pessoa(**dados)

print(px.nome)

p1.__dict__['nome'] = 'tnc!'
print(p1.__dict__)
print(vars(p1))
print(p1.nome)