'''class Caneta:
    def __init__(self,cor):
        self.cor_porra = cor

    def get_cor(self):
        print('GET_COR')
        return self.cor_porra

caneta = Caneta('Azul')
print(caneta.get_cor())
print(caneta.get_cor())
'''


class Caneta:
    def __init__(self,cor,nao):
        #private protected
        self.cor_sim = cor
        self.cor_nao = nao

    #usado para proteger o atributo, transformando o metodo no atributo
    @property
    def cor(self):
        return self.cor_sim
    
    #setter usado para modificar o valor da property
    @cor.setter
    def cor(self,valor):
        if valor == 'Rosa':
            raise ValueError('Não aceito esse valor.')
        self.cor_sim = valor

    @property
    def cor_tampa(self):
        return self.cor_nao

    @cor_tampa.setter
    def cor_tampa(self,valor):
        if valor == 'Fodase':
            raise ValueError('Não escreva essa porra!')
        self.cor_nao = valor

def mostrar(caneta):
    return caneta.cor

caneta = Caneta('Azul','Volei')
caneta.cor = 'Pink'
caneta.cor_tampa = 'Fodasee'
print(caneta.cor)
print(caneta.cor_tampa)