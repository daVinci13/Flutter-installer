#!/usr/bin/env python

import zipfile
import wget, os
import userpath
import ctypes,sys




def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    url = "https://storage.googleapis.com/flutter_infra/releases/stable/windows/flutter_windows_v1.9.1+hotfix.6-stable.zip"
    print("Downloading FLutter.....")
    wget.download(url, 'flutter.zip')

    print("Extracting FLutter.....")
    with zipfile.ZipFile('flutter.zip', "r") as zip_ref:
        zip_ref.extractall("C:\\")
    location = "C:\\flutter\\bin"

    userpath.append(location)
    #os.system('setx /M path "%path%;C:\\flutter\\bin"')
    print("Flutter has been added to Windows environment variables and will now restart. Please save your work!")
    input("Press Enter to reboot...")
    os.system("shutdown -t 0 -r -f")
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)