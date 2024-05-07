import os
import shutil
from pathlib import Path


BOOT_PATH = Path(__file__).parent

#file = open("Manipulando arquivos/Newfile.txt", "w")

#os.mkdir(BOOT_PATH/ "OS_SHUTIL")
#os.rename(BOOT_PATH/ "OS_SHUTIL", BOOT_PATH/ "os_shutil")
#os.remove(BOOT_PATH/ "os_shutil")
shutil.move(BOOT_PATH/ "teste.txt", BOOT_PATH/ "os_shutil" / "teste.txt")
