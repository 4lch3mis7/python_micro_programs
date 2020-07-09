import psutil

def pidof(name):
    name = name.lower()
    proc_dict = {}
    for i in psutil.process_iter(['name','pid']):
        proc = i.name().lower()
        pid = i.pid
        proc_dict.update({proc : pid})
    return proc_dict[name]

val = pidof('explorer.exe')
print(val)
