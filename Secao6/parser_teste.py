import re
from time import sleep
from pathlib import Path
from datetime import datetime

allTests = None
allTestsLength = None
cache_allTestsLength = None
init = 0

PADROES = {
    'pn': r'P/N\s*:\s*(.*)',
    'time': r'TIME\s*:\s*(.*)',
    'jig': r'JIG\s*:\s*(.*)',
    'result': r'RESULT\s*:\s*(.*)',
    'sw': r'S/W\s*:\s*(.*)',
    'imeino': r'IMEINO\s*:\s*(.*?)(?=\s*\w+\s*:|$)',
}

data_hoje = datetime.now().timestamp()
data_hoje = str(data_hoje)
def writeState(date,state,address = "C:\\Users\\josek\\Documents\\states.ini"):
    with open(address,"w",encoding="utf-8") as iniFile:
        iniFile.write(date+"-"+state)

def readState(address = "C:\\Users\\josek\\Documents\\states.ini"):
    with open(address,"r",encoding="utf-8") as iniFile:
        content = iniFile.readline()
        content = content.split("-")
        print(content)
        return content[-1]

def extrair_dados(bloco):
    dados = {}
    for chave, padrao in PADROES.items():
        match = re.search(padrao, bloco)
        if match:
            dados[chave] = match.group(1).strip()
    return dados

def checkIfFileExist():
    result = Path("C:\\Users\\josek\\Documents\\states.ini").exists()
    return result

def getCurrentFileLen():
    global allTests,allTestsLength
    with open("C:\\Users\\josek\\Documents\\DGS\\LOGS\\teste.txt",'r',encoding='utf-8') as f:
        content = f.read()
    allTests = content.split("#INIT\n")[1:]
    allTestsLength = len(allTests)

if checkIfFileExist():
    init = int(readState())

while True:
    getCurrentFileLen()
    if (cache_allTestsLength != allTestsLength) and (init != allTestsLength):
        for i in range(init,allTestsLength):
            singleTest = allTests[i]
            print(extrair_dados(singleTest))
            print("==================================================")
        str_allTestsLength = str(allTestsLength)
        writeState(data_hoje,str_allTestsLength)
        init = int(readState())
        cache_allTestsLength = allTestsLength
    
    print("=================ESPERANDO NOVO(S) TESTE(S)=================")
    sleep(4)
