import psutil
import time

def isprocess(name):
    proc_list = []
    c = 0
    for i in psutil.process_iter(['name']):
        proc = i.name()
        proc_list.append(proc)
    proc_count = len(proc_list)

    for process in proc_list:
        c = c+1
        if process.lower() == name.lower():
            return True
        else:
            if c == proc_count:
                return False

# print(isprocess('taskmgr.exe'))

