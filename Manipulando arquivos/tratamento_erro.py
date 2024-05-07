from pathlib import Path

BOOT_PATH = Path(__file__).parent


try:
    file = open(BOOT_PATH / "os_shutil")
except FileNotFoundError as execption:
    print("Arquivo não encontrado")
    print(execption)
except IsADirectoryError as execption:
    print("É um diretório")
    print(execption)
except PermissionError as execption:
    print("Sem permissão")
    print(execption)
except IOError as execption:
    print("Erro de I/O")
    print(execption)
except Exception as execption:
    print(f"Erro desconhecido: {execption}") 