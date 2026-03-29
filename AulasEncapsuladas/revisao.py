class Caneta:
    def __init__(self, cor, cor_tampa):
        self.cor_tinta = cor
        self.cor_tampa = cor_tampa
        self._cor_tinta = self.cor_tinta
        self._cor_tampa = self.cor_tampa
    
    @property
    def cor(self):
        return self.cor_tinta

    @cor.setter
    def cor(self,valor):
        if valor == 'ROSA':
            raise Exception('Não aceito cor rosa')
        self.cor_tinta = valor
        return self.cor_tinta


    @property
    def cor_tampa_get(self):
        return self.cor_tampa
    
    @cor_tampa_get.setter
    def cor_tampa_get(self, valor2):
        self.cor_tampa = valor2
        return self.cor_tampa
    
caneta = Caneta('AZUL','preto')
print(caneta.cor)
caneta.cor = 'lilás'
print(caneta.cor)
print(caneta.cor_tampa_get)
caneta.cor_tampa_get = 'fala baixo'
print(caneta.cor_tampa_get)