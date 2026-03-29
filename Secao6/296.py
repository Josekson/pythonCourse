from pathlib import Path
import csv


caminho = Path(__file__).parent
caminho_csv = Path.joinpath(caminho,'aulaHAHAHA.csv')

lista_clientes = [
    {"nome":"Josekson Goncalves","Endereco":"Alvorada 2"},
    {"nome":"Yasmin Ibernon","Endereco":"Lirio do vale"},
    {"nome":"Dante Goncalves","Endereco":"Redencao"},

]
title = lista_clientes[0].keys()

'''with open(caminho_csv,'w',encoding='utf-8') as file:
    csv_writer = csv.writer(file,lineterminator="\n")
    csv_writer.writerow(title)
    for i in lista_clientes:
        csv_writer.writerow(i.values())'''

'''title = ["nome","Endereco"]
with open(caminho_csv,'w',encoding='utf-8') as file:
    csv_writer = csv.DictWriter(file,fieldnames=title,lineterminator='\n')
    csv_writer.writeheader()
    for i in lista_clientes:
        csv_writer.writerow(i)'''

header = "nome,endereco\n"
texto = "josekson, alvorada2\nYasmin,Alvorada 1\nDante,redencao"
with open(caminho_csv,'w',encoding='utf-8') as file2:
    file2.write(header)
    file2.write(texto)