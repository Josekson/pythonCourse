import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME,'Desktop')
PASTA_ORGIGINAL = os.path.join(DESKTOP,'Hana_Documents')
NOVA_PASTA = os.path.join(DESKTOP,'NOVA_PASTA')

for root, dirs, files in os.walk(PASTA_ORGIGINAL):
    print(root.replace(PASTA_ORGIGINAL,NOVA_PASTA))
    os.makedirs(root.replace(PASTA_ORGIGINAL,NOVA_PASTA),exist_ok=True)
    for file in files:
        caminho_file = os.path.join(root,file)
        caminho_novo_file = os.path.join(
            root.replace(PASTA_ORGIGINAL,NOVA_PASTA),file
            )
        
        shutil.copy(caminho_file,caminho_novo_file) #é necessario mandar criar as pastas antes
        print(f'Copiando arquivo {caminho_novo_file}')