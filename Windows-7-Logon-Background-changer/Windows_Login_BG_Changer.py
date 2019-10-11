import ctypes, sys, os
from winreg import *

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    # Code of your program here
    def code1():
        #import module1

        # print (r"*** Reading from SOFTWARE\Microsoft\Windows\CurrentVersion\Run ***")
        aReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)

        print(r"*** Writing to SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI\Background ***")
        aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI\Background", 0,
                       KEY_WRITE)
        try:
            SetValueEx(aKey, "OEMBackground", 0, REG_DWORD, int(1))
        except EnvironmentError:
            print("Encountered problems writing into the Registry...")
        CloseKey(aKey)

        CloseKey(aReg)

    def code2():
        # import module2
        print("\n==================================================================")
        print("  ->  SIMPLE PYTHON PROGRAM TO CHANGE WINDOWS7 LOGON UI")
        print("                               by - PRASANT")
        print("\n==================================================================")

        import os
        import shutil

        # getting system drive
        sys_drive = os.getenv("SystemDrive")

        # print("\n" + "Enter the image path" + "\n(Example: D:\pictures\LogonUI.jpg)")
        # src = input("\nLogon screen source: ")

        def browse():
            from tkinter import filedialog
            from tkinter import Tk

            root = Tk()
            root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                       filetypes=(("jpeg files", "*.png",), ("all files", "*.*")))
            return root.filename

        print("\n"+"Press Enter to Browse Files...")
        input()
        src = browse()

        pre_dst = r"C:\Windows\System32\oobe\info\backgrounds"  # this is the destination directory
        dst = r"C:\Windows\System32\oobe\info\backgrounds\backgroundDefault.jpg"  # this is the destination file
        print(dst)

        try:  # try this first
            shutil.copy(src, dst)

        # make it first and then execute the same command again
        except FileNotFoundError:  # in case the directory doesnt exist,
            os.makedirs(pre_dst)  # make the directory and subdirectory first
            shutil.copy(src, dst)  # then execute the necessary command

        # THAT'S IT :)


    code1()
    code2()
    """
    
    print("Code of your program here!")
    try:
        # to execute a python program
        # os.system("python program.py")
    except:
        print("Error while executing python module.")
    
    """

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)