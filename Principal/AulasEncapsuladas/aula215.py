class Escritor:
    def __init__(self,nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self,nome):
        self._ferramenta = nome


class FerramentaDeEscrever:
    def __init__(self,nome):
        self.nome = nome
    
    def escrever(self):
        return f'{self.nome} está escrevendo'

escritor = Escritor('Luiz')
caneta = FerramentaDeEscrever('Bic')
maquina_escrever = FerramentaDeEscrever('Máquina')
escritor.ferramenta = maquina_escrever


print(escritor.ferramenta.nome)
print(caneta.escrever())
print(escritor.ferramenta.escrever())

#Cria uma variavel com None, Cria um property e um setter para essa variavel
# atribua à essa variavel a classe inteira, assim voce tera tudo dessa classe nova
#na variavel None