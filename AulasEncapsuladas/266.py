from dataclasses import dataclass

@dataclass
class Pessoa:
    nome:str
    sobrenome:str
    print('To no init')

    def __post_init__(self):
        print('Pós init')

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


    @property
    def primeiro_nome(self):
        return self.nome
    
    @primeiro_nome.setter
    def primeiro_nome(self, valor):
        self.nome = valor


if __name__ == '__main__':
    p1 = Pessoa('Josekson','Silva')
    print(p1)
    print(p1.nome_completo())
    print(p1.primeiro_nome)
    p1.primeiro_nome = 'Juka'
    print(p1.primeiro_nome) 