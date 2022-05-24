import socket
import sys
import os

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Client socket creation")
    server_address = ('localhost', 10000)
except socket.herror:
    print("Failed to create the client socket")
    sys.exit(-1)

def SendMessage(message):
    messageEncoded = message.encode()
    sock.sendto(messageEncoded, server_address)
    print(f"Sending {message} message to server")

def ReceiveMessage():
    data, server = sock.recvfrom(4096)
    return data

def ClientGet():
    if "Error" in ReceiveMessage().decode():
        print("The file doesn't exist")
        return
    f = open(msg.split(' ',1)[1], "wb")

    bytes = b''
    data = True
    sock.settimeout(2)       
    try:
        while data:       
            data, server = sock.recvfrom(1024)
            bytes += data
    except socket.timeout:
        f.write(bytes)
        f.close()

def ClientPut():
    if os.path.isfile(msg.split(' ',1)[1]):
        SendMessage("File exists.")
        f = open(msg.split(' ',1)[1], "rb")
        data = f.read(1024)
        while data:
            sock.sendto(data, server_address)
            print ("sending ...")
            data = f.read(1024)
        f.close()
    else:
        SendMessage("Error: file not found")
    sock.settimeout(5)
    data, server = sock.recvfrom(4096)
    print(data.decode())
    
def ClientList():
    print(ReceiveMessage().decode())

def ClientExit():
    print("Client socket closed, not sending any message to Server.")
    sock.close()
    sys.exit(0)

while True:
    try:
        msg = input("What message do you want to send? (get 'file_name', put 'file_name', list, exit): ")
        SendMessage(msg)

        if "get" in msg:
            ClientGet()
        elif "put" in msg:
            ClientPut()
        elif "list" in msg:
            ClientList()
        elif "exit" in msg:
            ClientExit()
        else:
            print(ReceiveMessage().decode())
    except TimeoutError:
        pass