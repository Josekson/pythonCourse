payload ={
  "payload": {
    "results": {
      "anyName1": "2592912038M06",
      "anyName2": "2592912039M01"
    }
  }
}

primeiro = payload["payload"]["results"]['anyName1']
ultimo = payload["payload"]["results"]['anyName2']

prefixo_primeiro = primeiro[:11]

sufixo_primeiro = primeiro[11:]

prefixo_ultimo = ultimo[:11]
sufixo_ultimo = ultimo[11:]

def sequencia_primeiro_valor(primeiro):

    prefixo_primeiro = primeiro[:11]

    sufixo_primeiro = primeiro[11:]

    sufixo_segundo = int(sufixo_primeiro) + 1
    segundo = prefixo_primeiro + f'{sufixo_segundo:02d}' #valor ultimate

    sufixo_terceiro = sufixo_segundo + 1
    terceiro = prefixo_primeiro + f'{sufixo_terceiro:02d}' #valor ultimate

    return segundo, terceiro


def create_payload(primeiro,segundo,terceiro,ultimo):
    payload = {
        'payload':[
            primeiro,
            segundo,
            terceiro,
            ultimo
        ]
    }
    return payload

if (prefixo_primeiro == prefixo_ultimo) or (sufixo_ultimo == "00"):
    tupla = sequencia_primeiro_valor(primeiro)
    payload = create_payload(primeiro,tupla[0],tupla[1],ultimo)
    print(payload)

else:
    cont = 0
    lista = []
    sufixo = []
    while sufixo_ultimo != "00" and cont<2:
        calculo = int(sufixo_ultimo) - 1
        sufixo.append(calculo) #começa do maior sufixo depois do ultimo valor
        lista.append(prefixo_ultimo + f'{sufixo[cont]:02d}')
        sufixo_ultimo = f'{calculo:02d}'
        print(sufixo_ultimo)
        cont += 1
    print(len(lista))
    
