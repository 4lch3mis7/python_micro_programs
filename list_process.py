import psutil

def list_process():
    print("ProcessName (ProcessID)")
    print("-----------------------")
    for i in psutil.process_iter(['name','pid']):
        proc = i.name()
        pid = i.pid
        print(proc, "("+ str(pid) +")") 
