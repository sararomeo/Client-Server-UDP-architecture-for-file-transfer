import socket as sk
from socket import *
import sys
import time
import os

try:
    # UDP socket creation
    sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    print("Client socket creation")
    # Defining the server address to send messages
    server_address = ('localhost', 10000)
except sk.error:
    print("Failed to create the client socket")
    sys.exit()

    
def SendMessage(message):
    messageEncoded = message.encode()
    sock.sendto(messageEncoded, server_address)
    print("Sending \"%s\" message to server" % message)

def ReceiveMessage():
    data, server = sock.recvfrom(4096)
    time.sleep(2)
    dataDecoded = data.decode()
    print(dataDecoded)
    return data


def ReceiveFile():
    data, server = sock.recvfrom(1024)
    f = open(data, "wb")

    data, server = sock.recvfrom(1024)
    try:
        while data:       
            f.write(data)
            sock.settimeout(2)
            data, server = sock.recvfrom(1024)
    except timeout:
        f.close()
        print("nosdasdasdassda")
        sock.settimeout(20)

def SendFile():
    if os.path.isfile(msg.split()[1]):
        SendMessage("File exists.")
        f = open(msg.split()[1], "rb")
        data = f.read(1024)
        while data:
            if sock.sendto(data, server_address):
                print ("sending ...")
                data = f.read(1024)
        f.close()
    else:
        SendMessage("Error: file not found")

def ClientGet():
    ReceiveMessage()
    message = ReceiveMessage()
    if message.decode().__contains__("Error"):
        print("Wrong file name, retry")
        return
    ReceiveFile()
    print("xd")

def ClientPut():
    SendFile()

def ClientList():
    while True:
        message = ReceiveMessage()
        if message.__contains__(b"List sent"):
            break
    SendMessage("List received")


def ClientExit():
    print("Client socket closed, not sending any message to Server.")
    sock.close()
    sys.exit()

while True:
    msg = input("What message do you want to send? (get 'file_name', put 'file_name', list, exit): ")
    SendMessage(msg)
    if msg.__contains__("get"):
        ClientGet()
    elif msg.__contains__("put"):
        ClientPut()
    elif msg.__contains__("list"):
        ClientList()
    elif msg.__contains__("exit"):
        ClientExit()
    else:
        ReceiveMessage()
        print("Command not found")
