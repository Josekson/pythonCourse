import os


caminho_arquivo = "C:\\Users\\josek\\Documents\\Curso_Python\\"
caminho_arquivo += "arquivo617.txt"

with open(caminho_arquivo,'w+',encoding='utf-8') as file:
    file.write('Me dá a vaga de analista, Jabil\n')
    file.write('Me dá a vaga de analista, Jabil\n')
    file.writelines(
        ('Linha3\n','Linha 4\n')
    )
    file.seek(0,0) #Move cursor para a origem
    print(file.read()) # Ler tudo
    print('Lendo linha por linha:')
    file.seek(0,0) #Move cursor para a origem
    print(file.readline(),end='') # Ler linha por linha a cada vez que é invocado
    print(file.readline()) # Ler linha por linha a cada vez que é invocado
    file.seek(0,0)
    print('Usando o FOR:')
    for linha in file.readline():
        print(linha,end='')

print('Leitura abaixo:')

with open(caminho_arquivo,'r',encoding='utf-8') as file:
    print(file.read())

# os.remove("arquivo617.txt") -> usado para remover o arquivo
os.rename(caminho_arquivo,"C:\\Users\\josek\\Documents\\Curso_Python\\testando\\aula_rename_move.txt")