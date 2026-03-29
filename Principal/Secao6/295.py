from pathlib import Path
import csv

caminho = Path(__file__).parent
print(caminho)

caminho_csv = Path.joinpath(caminho,'exemplo.csv')
print(caminho_csv)

'''with open(caminho_csv,'r') as csv_file:
    conteudo_csv = csv.reader(csv_file)
    #list_conteudo_csv = list(conteudo_csv)
    for i in conteudo_csv:
        print(i)'''


with open(caminho_csv,'r') as csv_file:
    conteudo_csv = csv.DictReader(csv_file,skipinitialspace=True)
    #list_conteudo_csv = list(conteudo_csv)
    for i in conteudo_csv:
        print(i)
    