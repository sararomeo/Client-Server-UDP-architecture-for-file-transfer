import socket
import sys
import os

try:
    # UDP socket creation
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #sock.settimeout(1)
    print("Client socket creation")
    # Defining the server address to send messages
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
    dataDecoded = data.decode()
    print(f"Message received: {dataDecoded}")
    return data

def ReceiveFile():
    data, server = sock.recvfrom(1024)
    f = open(data.decode(), "wb")

    bytes = b''
    sock.settimeout(2)       
    try:
        while data:       
            data, server = sock.recvfrom(1024)
            bytes += data
    except socket.timeout:
        sock.settimeout(2)
    finally:
        f.write(bytes)
        f.close()

def SendFile():
    if os.path.isfile(msg.split(' ',1)[1]):
        SendMessage("File exists.")
        f = open(msg.split(' ',1)[1], "rb")
        data = f.read(1024)
        while data:
            sock.sendto(data, server_address)
            print ("Sending file")
            data = f.read(1024)
        f.close()
    else:
        SendMessage("Error: file not found")

def ClientGet():
    ReceiveMessage()
    message = ReceiveMessage()
    if "Error" in message.decode():
        print("Wrong file name, retry")
        return
    ReceiveFile()

def ClientPut():
    ReceiveMessage()
    SendFile()

def ClientList():
    while True:
        message = ReceiveMessage()
        if "List sent" in message:
            break


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
            ReceiveMessage()
    except Exception:
        pass
