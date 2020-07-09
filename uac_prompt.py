import ctypes
import sys

def uac_prompt():
    import os
    if is_admin():
        # Program here
        os.system("net session")
    else:
        # Re-run the program with admin previliges
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__,None, 1)
