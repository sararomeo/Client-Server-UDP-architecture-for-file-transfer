import socket as sk
import sys
import time

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
    return dataDecoded


def ReceiveFile():
    data, server = sock.recvfrom(1024)
    f = open(data, "wb")

    while True:
        data, server = sock.recvfrom(1024)
        if data.__eq__(b"EOF"):
            print("not data")
            f.close()
            break
 
        print("prima write")
        f.write(data)
        time.sleep(2)
        print("dopo write")   


def ClientGet():
    while True:
        ReceiveMessage()
        print("--" + ReceiveMessage() + "--" + msg.split()[1])
        ReceiveFile()
        print("xd")
        break

def ClientPut():
    ReceiveMessage()

def ClientList():
    while True:
        ReceiveMessage()
        if not ReceiveMessage():
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
