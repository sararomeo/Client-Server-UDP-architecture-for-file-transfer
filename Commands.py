'''
This file contains all the functions used by the client and the server
'''
import os
import sys

def SendMessage(message, name, address, sock):
    messageEncoded = message.encode()
    sock.sendto(messageEncoded, address)
    print(f"Sending {message} message to {name}")

def ReceiveMessage(sock):
    data, addr = sock.recvfrom(4096)
    return data

def ClientGet(sock, message):
    if "Error" in ReceiveMessage(sock).decode():
        print("The file doesn't exist")
        return
    f = open(message.split(' ',1)[1], "wb")

    bytes = b''
    data = True
    sock.settimeout(2)       
    try:
        while data:       
            data, server = sock.recvfrom(1024)
            bytes += data
    except TimeoutError:
        f.write(bytes)
        f.close()

def ServerGet(filename, sock, address):
    print("Correct command, trying to get your file..")
    if os.path.isfile(filename):
        SendMessage("File exists.", "client", address, sock)
        f = open (filename, "rb") 
        data = f.read(1024)
        while data:
            sock.sendto(data, address)
            print ("sending ...")
            data = f.read(1024)
        f.close()
    else:
        SendMessage("Error: file doesn't exist.", "client", address, sock)

def ClientPut(message, sock, address):
    if os.path.isfile(message.split(' ',1)[1]):
        SendMessage("File exists.", "server", address, sock)
        f = open(message.split(' ',1)[1], "rb")
        data = f.read(1024)
        while data:
            sock.sendto(data, address)
            print ("sending ...")
            data = f.read(1024)
        f.close()
    else:
        SendMessage("Error: file not found",  "server", address, sock)
    sock.settimeout(5)
    #data, server = sock.recvfrom(4096)
    #print(data.decode())
    print(ReceiveMessage(sock).decode())

def ServerPut(filename, address, sock):
    print("Correct command, trying to put your file..")
    if "Error" in ReceiveMessage(sock).decode():
        SendMessage("File not uploaded", "client", address, sock)
        return
    print("Starting the upload")
    f = open(filename, "wb")
    bytes = b''
    data = True
    sock.settimeout(2)
    try:
        while data:
            data, server = sock.recvfrom(1024)
            bytes += data
    except TimeoutError:
        f.write(bytes)
        SendMessage("File uploaded", "client", address, sock)
        f.close()

def ClientList(sock):
    print(ReceiveMessage(sock).decode())

def ServerList(sock, address):
    print("Correct command, trying to get available files list..")
    path = os.getcwd()
    F = os.listdir(path)
    filesList = []
    for file in F:
        filesList.append(file)
    filesList.remove('Server.py')
    filesListStr = str(filesList)
    filesListEn = filesListStr.encode()
    sock.sendto(filesListEn, address)

def Exit(sock, nameHost, nameRemote):
    print(f"{nameHost} socket closed, not sending any message to {nameRemote}.")
    sock.close()
    sys.exit(0)