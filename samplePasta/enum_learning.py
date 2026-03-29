import enum

#Direcoes = enum.Enum('Direcoes',['ESQUERDA','DIREITA'])

class Direcoes(enum.Enum):
    DIREITA = enum.auto() #ENUMERA AUTOMATICAMENTE
    ESQUERDA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()

print(Direcoes.DIREITA.name)
print(Direcoes.ESQUERDA.name)

def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise Exception('Esta direcao não existe')
    print(f'Movendo para {direcao.name} ({direcao.value})')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)
#mover('lado')