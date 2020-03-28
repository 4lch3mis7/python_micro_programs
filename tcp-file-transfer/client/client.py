import socket
import time

def socket_connect():
    try:
        global host
        global port
        global s
        s = socket.socket()
        host = '127.0.0.1'
        port = 8080
        s.connect((host, port))
        print("\n[*] Connection established successfully.")
    except socket.error as msg:
        print("\n[*] Connection Error: ", msg)
        time.sleep(5)
        connect_socket()


def recieve_data():
    # Recieving and Decoding data
    try:
        global data
        global file_name
        
        s.settimeout(None)
        file_name = s.recv(1000).decode('utf-8')
        
        s.settimeout(None)
        data = s.recv(10000000000)
    except socket.error as msg:
        print("\n[*]", msg)
    except:
        print("\n[*] Decoding Error")
    
   


# creating space to save file
def write_files():
    try:
        global data
        file_recieved = open(file_name, 'wb')
        file_recieved.write(data)
        file_recieved.close()
        print("\n[*] File recieved succesfully.", file_name)
    except OSError as msg:
        print("[*] Storage Error: ", msg)
        time.sleep(5)            
        


socket_connect()
recieve_data()
write_files()

s.close()





