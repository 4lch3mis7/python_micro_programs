import socket
import time

def socket_create():
    try:
        global host
        global port 
        global s
        s = socket.socket()
        host = '127.0.0.1'
        port = 8080
    except socket.error as msg:    
        print("[*] Socket Creation Error: ", msg)


def socket_bind():
    try:
        global host
        global port
        global s
        s.bind((host,port))
    except socket.error as msg:
        print("[*] Error Binding Socket: ", msg)
        s.close()
        time.sleep(5)
        socket_bind()
       
def accept_connections():
    try:
        global conn
        global addr
        s.listen(1)
        conn, addr = s.accept()
        print(f"[*] Connection has been established")
    except socket.error as msg:
        print("[*] Error Accepting Connection: ", msg)


# detecting file name
def detect_file_name(file_path):
    #file_path = '/home/prasant/Desktop/file-transfer/file.txt'
    l = file_path.split('/')  # Not for windows
    last_index = len(l) - 1
    file_name = l[last_index]
    return file_name


def send_files():
    # Reading file
    try:
        file_path = str(input("Enter file path: ")) 
        file_name = detect_file_name(file_path).encode('utf-8')
        file_buffer = open(file_path, 'rb')
        data = file_buffer.read()       
    except (OSError, IOError) as msg:
        print("[*] ", msg)
        
    # Sending file
    try:
        conn.send(file_name)
        time.sleep(0.1)
        conn.send(data)
        file_buffer.close()
        print("\n[*] File has been sent successfully: ")
    except OSError as msg:
        print("\n[*] Sending Error: ", msg)
        

socket_create()
socket_bind()
accept_connections()
send_files()

conn.close()
s.close()

 
 
