import socket as sk
import sys
import os

BUFFER_SIZE=4096

try:    
    sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    server_address = ('localhost', 10000)
    print ('\n\rStarting up on %s port %s' % server_address)
    sock.bind(server_address)
    print("Successful binding. Waiting for Client now.")
except sk.herror:
    print("Failed to create socket")
    sys.exit(-1)

def SendMessageToClient(msg):
    msgEn = msg.encode('utf-8')
    sock.sendto(msgEn, clientAddr)
    print(f'Sent {msg} message to client')
    
def ReceiveMessageFromClient():
    data, server = sock.recvfrom(BUFFER_SIZE)
    dataDec = data.decode('utf8')
    print(dataDec)
    return data

def ReceiveFile():
    f = open(t[1], "wb")
    bytes = b''
    data = True
    sock.settimeout(2)
    try:
        while data:
            data, server = sock.recvfrom(1024)
            bytes += data
    except sk.timeout:
        sock.settimeout(2)
    finally:
        f.write(bytes)
        f.close()

def ServerList():
    SendMessageToClient("Correct command, trying to get available files list..")
    path = os.getcwd()
    F = os.listdir(path)
    filesList = []
    for file in F:
        filesList.append(file)
    filesList.remove('Server.py')
    filesListStr = str(filesList)
    filesListEn = filesListStr.encode('utf-8')
    sock.sendto(filesListEn, clientAddr)
    SendMessageToClient("List sent from Server")

def ServerGet(filename):
    SendMessageToClient("Correct command, trying to get your file..")
    if os.path.isfile(filename):
        SendMessageToClient("File exists.")
        SendMessageToClient(filename)
        f = open (filename, "rb") 
        data = f.read(1024)
        while data:
            sock.sendto(data,clientAddr)
            print ("sending ...")
            data = f.read(1024)
        f.close()
    else:
        SendMessageToClient("Error: file doesn't exist.")

def ServerPut():
    SendMessageToClient("Correct command, trying to put your file..")
    message = ReceiveMessageFromClient()
    if "Error" in message.decode():
        SendMessageToClient("Wrong file name, retry")
        return
    ReceiveFile()
    SendMessageToClient("File received.")

def ServerExit():
    print("Server socket closed, not sending any message to Client.\n\n")
    sock.close()
    sys.exit(0)

while True:
    print('\n\r\tWaiting to receive message...')
    try:
        data, clientAddr = sock.recvfrom(BUFFER_SIZE)
        text = data.decode('utf8')
        t = text.split(' ',1)
        command = t[0]
        if command == "get":
            fileName = t[1]
            ServerGet(fileName)
        elif command == "put":
            ServerPut()
        elif command == "list":
            ServerList()
        elif command == "exit":
            ServerExit()
        else:
            SendMessageToClient("Unknown input.")
    except Exception:
        pass

