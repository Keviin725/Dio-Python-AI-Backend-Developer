import csv
from pathlib import Path

BOOT_PATH = Path(__file__).parent

try:
    with open(BOOT_PATH / 'pessoas.csv', 'w', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['Nome', 'Idade'])
        escritor.writerow(['Lucas', 26])
        escritor.writerow(['João', 30])
        escritor.writerow(['Maria', 22])


except IOError as execption:
    print(f"Erro de I/O {execption}")


try:
    with open(BOOT_PATH / 'pessoas.csv', 'r', encoding='utf-8') as entrada:
        leitor = csv.reader(entrada)
        for linha in leitor:
            print(linha)
except IOError as execption:
    print(f"Erro de I/O {execption}")