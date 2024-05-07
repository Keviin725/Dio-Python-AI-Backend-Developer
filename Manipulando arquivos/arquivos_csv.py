import csv
from pathlib import Path

BOOT_PATH = Path(__file__).parent
COLUNA_NOME = 0
COLUNA_IDADE = 1

'''try:
    with open(BOOT_PATH / 'pessoas.csv', 'w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['Nome', 'Idade'])
        escritor.writerow(['Lucas', 26])
        escritor.writerow(['João', 30])
        escritor.writerow(['Maria', 22])


except IOError as execption:
    print(f"Erro de I/O {execption}")


 '''   
try:
    with open(BOOT_PATH / 'pessoas.csv', 'r', newline='', encoding='utf-8') as entrada:
        leitor = csv.reader(entrada)
        for idx, linha in enumerate(leitor):
            if idx == 0:
                continue
            if len(linha) > max(COLUNA_NOME, COLUNA_IDADE):
                print(f"Nome: {linha[COLUNA_NOME]}")
                print(f"Idade: {linha[COLUNA_IDADE]}")
            else:
                print("Linha não tem colunas suficientes")
except IOError as execption:
    print(f"Erro de I/O {execption}")
'''    
try:
    with open(BOOT_PATH / 'pessoas.csv', 'r', newline='', encoding='utf-8') as entrada:
        leitor = csv.DictReader(entrada)
        for linha in leitor:
            print(linha['Nome'], linha['Idade'])
except IOError as execption:
    print(f"Erro de I/O {execption}")'''