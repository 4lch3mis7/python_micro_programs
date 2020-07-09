import os
from isprocess import *

homedrive = os.getenv('HOMEDRIVE')
appdata = os.getenv('AppData')
path_firefox = homedrive + r'\Program Files\Mozilla Firefox'
path_chrome = appdata + r'\Google\Chrome'
path_brave = homedrive + r'\Program Files (x86)\BraveSoftware'


print(path_chrome)

if isprocess('explorer.exe'):
    if os.path.exists(path_firefox or path_chrome or path_brave):
        print("Not an AV")



    
