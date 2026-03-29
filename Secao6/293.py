import json

FILE_NAME = 'teste.json'

texto = {
    "company":"Jabil",
    "Matricula":4211331,
    "Cargo":[
        "imbecil",
        "ze nada"
    ]
}

with open(FILE_NAME,'w',encoding='utf-8') as f:
    json.dump(texto,f,ensure_ascii=False,indent=2) #Pego algo e faço virar um json


FILE_NAME = 'C:\\Users\\josek\\Documents\\Curso_Python\\teste.json'
with open(FILE_NAME,'r') as f2: # pega algo que ja era json e transforma numa string
    var = json.load(f2)
print(var)