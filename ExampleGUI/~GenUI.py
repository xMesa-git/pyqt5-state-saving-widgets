import os

pyuic = "D:/Python3.9.10/Scripts/pyuic5.exe"

try:
    command = f"{pyuic} example.ui -o WindowGUI.py"
    result = os.system(command)
    if result == 0:
        print('Done.')
except Exception as e:
    print(f'Error {e}')
