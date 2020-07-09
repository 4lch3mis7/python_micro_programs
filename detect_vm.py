import os

startup = os.getenv('AppData') + r'\Microsoft\Windows\Start Menu\Programs\Startup'
os.chdir(startup)
os.system('dir & pause')
os.system("echo cmd > command.exe")
os.system('dir & pause')
