from pathlib import Path

BOOT_PATH = Path(__file__).parent

try:

    with open(BOOT_PATH / 'lorem.txt', 'r') as arquivo:
        print(arquivo.read())
except IOError as execption:
    print(f"Erro de I/O {execption}")

'''
try:
    with open(BOOT_PATH / 'arquivo.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write('Escrevendo no arquivo')
except IOError as execption:
    print(f"Erro de I/O {execption}")
'''
try:
    with open(BOOT_PATH / 'arquivo.txt', 'r', encoding='ascii') as arquivo:
        print(arquivo.read())
except IOError as execption:
    print(f"Erro de I/O {execption}")
except UnicodeDecodeError as execption:
    print(f"Erro de codificação {execption}")