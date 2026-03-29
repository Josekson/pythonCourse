import json
'''
pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('jason.json','w',encoding='utf-8') as file:
    json.dump(
        pessoa,file,ensure_ascii=False,
        indent=2
        )
     '''

with open('jason.json','r',encoding='utf-8') as file:
    pessoa = json.load(file)
print(pessoa)
print(type(pessoa))