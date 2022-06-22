import shutil
import os
import winreg

from os import listdir
from os.path import isfile, join, basename
from pathlib import Path

dirPath = r"C:\Vip"
lista_arquivos = os.listdir("C:\Vip")

path = Path("C:\Vip\Oldfiles");path.mkdir(parents=True, exist_ok=True)

path = Path("C:\Vip\Oldfiles\Clients");path.mkdir(parents=True, exist_ok=True)
path = Path("C:\Vip\Oldfiles\DB");path.mkdir(parents=True, exist_ok=True)
path = Path("C:\Vip\Oldfiles\Logs");path.mkdir(parents=True, exist_ok=True)
path = Path("C:\Vip\Oldfiles\RegisteredClients");path.mkdir(parents=True, exist_ok=True)


def move(path_origem, path_destino):
    for item in [join(path_origem, f) for f in listdir(path_origem) if isfile(join(path_origem, f))]:
        #print(item)
        shutil.move(item, join(path_destino, basename(item)))
        print('Movido de:"{}" Para: -> "{}"'.format(item, join(path_destino, basename(item))))

if __name__ == "__main__":
    move("C:\Vip", "C:\Vip\Oldfiles")
    move("C:\Vip\Clients", "C:\Vip\Oldfiles\Clients")
    move("C:\Vip\DB", "C:\Vip\Oldfiles\DB")
    move("C:\Vip\Logs", "C:\Vip\Oldfiles\Logs")
    move("C:\Vip\RegisteredClients", "C:\Vip\Oldfiles\RegisteredClients")

shutil.rmtree("C:\Vip\Clients")
shutil.rmtree("C:\Vip\DB")
shutil.rmtree("C:\Vip\Logs")
shutil.rmtree("C:\Vip\RegisteredClients")

os.rmdir("C:\Vip\Clients")
os.rmdir("C:\Vip\DB")
os.rmdir("C:\Vip\Logs")
os.rmdir("C:\Vip\RegisteredClients")

dirPath = r"C:\Vip"
os.remove('libeay32.dll');('pmtg.dll');('ssleay32.dll');('VipSQLite.exe');('VipSQLite.map');('bugreport.txt');('LogErroDetalhado.txt')

Key_Name = r'Software\ClubPetro'
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, Key_Name, 0, winreg.KEY_ALL_ACCESS)
winreg.DeleteKey(key, '')