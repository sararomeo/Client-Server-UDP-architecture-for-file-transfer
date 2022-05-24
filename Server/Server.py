from http import client
import socket
import sys
import os
from .. import Commands

try:    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_address = ('localhost', 10000)
    print (f"\n\r starting up on {client_address[0]} port {client_address[1]}")
    sock.bind(client_address)
    print("Successful binding. Waiting for Client now.")
except socket.herror:
    print("Failed to create socket")
    sys.exit(-1)

'''
def SendMessageToClient(msg):
    msgEn = msg.encode('utf-8')
    sock.sendto(msgEn, clientAddr)
    print(f'Sent {msg} message to client')

def ReceiveMessageFromClient():
    data, server = sock.recvfrom(BUFFER_SIZE)
    #dataDec = data.decode('utf8')
    #print(dataDec)
    return data

def ServerGet(filename):
    print("Correct command, trying to get your file..")
    if os.path.isfile(filename):
        SendMessageToClient("File exists.")
        #SendMessageToClient(filename)
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
    print("Correct command, trying to put your file..")
    if "Error" in ReceiveMessageFromClient().decode():
        SendMessageToClient("File not uploaded")
        return
    print("Starting the upload")
    f = open(t[1], "wb")
    bytes = b''
    data = True
    sock.settimeout(2)
    try:
        while data:
            data, server = sock.recvfrom(1024)
            bytes += data
    except TimeoutError:
        f.write(bytes)
        SendMessageToClient("File uploaded")
        f.close()

def ServerList():
    print("Correct command, trying to get available files list..")
    path = os.getcwd()
    F = os.listdir(path)
    filesList = []
    for file in F:
        filesList.append(file)
    filesList.remove('Server.py')
    filesListStr = str(filesList)
    filesListEn = filesListStr.encode('utf-8')
    sock.sendto(filesListEn, clientAddr)
    #SendMessageToClient("List sent from Server")
    #ReceiveMessageFromClient()

def ServerExit():
    print("Server socket closed, not sending any message to Client.")
    sock.close()
    sys.exit(0)
'''

while True:
    try:
        print('\n\r Waiting to receive message...')
        #data, clientAddr = sock.recvfrom(4096)
        #text = data.decode()
        #text = Commands.ReceiveMessage(sock).decode()
        #t = text.split(' ',1)
        t = Commands.ReceiveMessage(sock).decode().split(' ',1)
        command = t[0]
        if command == "get":
            #fileName = t[1]
            Commands.ServerGet(t[1], sock, client_address)
        elif command == "put":
            Commands.ServerPut(t[1], client_address, sock)
        elif command == "list":
            Commands.ServerList(sock, client_address)
        elif command == "exit":
            Commands.Exit(sock, "server", "client")
        else:
            Commands.SendMessage("Unknown input.", "client", client_address, sock)
    except TimeoutError:
        pass