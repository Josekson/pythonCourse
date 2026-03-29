def adiciona_clientes(nome,lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista
# Nunca coloque um parâmetro mutável numa função, pois ele sempre será o mesmo.


cliente1 = adiciona_clientes('Josekson')
print(adiciona_clientes('Dante',cliente1))

cliente2 = adiciona_clientes('Faker')
print(adiciona_clientes('Chovy',cliente2))