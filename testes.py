import winreg

Key_Name = r'Software\ClubPetro'
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, Key_Name, 0, winreg.KEY_ALL_ACCESS)
winreg.DeleteKey(key, '')