import shutil
import os
from os import listdir
from os.path import isfile, join, basename
from pathlib import Path

lista_arquivos = os.listdir("C:\Vip")

dirPath = r"C:\Vip"

path = Path("C:\Vip\Oldfiles")
path.mkdir(parents=True, exist_ok=True)

dirPath = r"C:\VipOldfiles"

path = Path("C:\Vip\Oldfiles\Clients")
path.mkdir(parents=True, exist_ok=True)
path = Path("C:\Vip\Oldfiles\DB")
path.mkdir(parents=True, exist_ok=True)
path = Path("C:\Vip\Oldfiles\Logs")
path.mkdir(parents=True, exist_ok=True)
path = Path("C:\Vip\Oldfiles\RegisteredClients")
path.mkdir(parents=True, exist_ok=True)



