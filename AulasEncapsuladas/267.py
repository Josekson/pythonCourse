from dataclasses import dataclass

@dataclass(init=False)
class Pessoa:
    nome:str
    sobrenome:str
    #print('To no init')

    def __init__(self,nome:str,sobrenome:str):
        self.nome = nome
        self.sobrenome = sobrenome
        print('To no init')
    
    def __post_init__(self):
        print('To no pos init')

if __name__ == '__main__':
    p1 = Pessoa('Josekson','Silva')

