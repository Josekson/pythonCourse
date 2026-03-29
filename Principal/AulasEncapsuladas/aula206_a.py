import json

CAMINHO_ARQUIVO = 'classe.json'
class Cachorro():
    def __init__(self,raca,cor,idade):
        self.raca = raca
        self.cor = cor
        self.idade = idade

chowchow = Cachorro('chowchow','amarelo',3)

dicionario = [chowchow.__dict__]

with open(CAMINHO_ARQUIVO,'w',encoding = 'utf-8') as file:
    json.dump(dicionario,file,indent=2)
