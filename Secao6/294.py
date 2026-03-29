from pathlib import Path

caminho_root = Path()
print(caminho_root.absolute())

caminho_arquivo = Path(__file__)
print(caminho_arquivo.parent)

pai = caminho_arquivo.parent

nova_pasta = Path.joinpath(pai,'NovaSecao')

print(nova_pasta)

print(Path.home())
new_way = Path.joinpath(Path.home(),'Desktop','jemsms.txt')
print(new_way)
new_way2 = Path.home() / 'caminho_path' / 'jemsms.txt'
print(new_way2)
new_way.touch() #Cria arquivo
#new_way.unlink() # exlcui
texto = '''De tudo, ao meu amor serei atento
Antes, e com tal zelo, e sempre, e tanto
Que mesmo em face do maior encanto
Dele se encante mais meu pensamento.Quero vivê-lo em cada vão momento
E em louvor hei de espalhar meu canto
E rir meu riso e derramar meu pranto
Ao seu pesar ou seu contentamento.E assim, quando mais tarde me procure
Quem sabe a morte, angústia de quem vive
Quem sabe a solidão, fim de quem amaEu possa me dizer do amor (que tive):
Que não seja imortal, posto que é chama
Mas que seja infinito enquanto dure.'''
new_way.write_text(texto)
with new_way.open('a+') as file:
    file.write('QUERO SER ESPECIALISTA\n')