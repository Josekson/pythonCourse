import json
from aula206_a import Cachorro, CAMINHO_ARQUIVO

with open(CAMINHO_ARQUIVO,'r',encoding = 'utf-8') as file:
    dicionario = json.load(file)

objeto = Cachorro(**dicionario[0])
print(objeto.raca)