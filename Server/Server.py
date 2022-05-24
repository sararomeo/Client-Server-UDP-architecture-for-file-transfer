import socket as sk
import sys
import os

BUFFER_SIZE=4096

# UDP datagram socket creation at server's startup
try:    
    sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    sock.settimeout(1)
    # localhost current IP address (I guess), port 10000
    server_address = ('localhost', 10000)
    print ('\n\rStarting up on %s port %s' % server_address)
    # port associated to socket
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

# creates a list with all available files
def ServerList():
    SendMessageToClient("Correct command, trying to get available files list..")
    # gets current directory
    path = os.getcwd()
    # gets the list of all files and dir in path dir
    F = os.listdir(path)
    # filesList contains just files
    filesList = []
    for file in F:
        filesList.append(file)
    filesList.remove('Server.py')
    filesListStr = str(filesList)
    filesListEn = filesListStr.encode('utf-8')
    sock.sendto(filesListEn, clientAddr)
    SendMessageToClient("List sent from Server")

#if exists, gets file from server dir and sends msg to client, else sends error
def ServerGet(filename):
    SendMessageToClient("Correct command, trying to get your file..")
    if os.path.isfile(filename):
        SendMessageToClient("File exists.")
        #get
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


#La ricezione di un messaggio put contenente il file da caricare sul server e
#l’invio di un messaggio di risposta con l’esito dell’operazion
def ServerPut():
    SendMessageToClient("Correct command, trying to put your file..")
    message = ReceiveMessageFromClient()
    if "Error" in message.decode():
        print("Wrong file name, retry")
        return
    ReceiveFile()

def ServerExit():
    print("Server socket closed, not sending any message to Client.\n\n")
    sock.close()
    sys.exit(0)

# listening for incoming datagrams
print('\n\r\tWaiting to receive message...')
while True:
    try:
        data, clientAddr = sock.recvfrom(BUFFER_SIZE)
        text = data.decode('utf8')
        t = text.split(' ',1)
        command = t[0]
        if command == "get":
            fileName = t[1]
            ServerGet(fileName)
            print('\n\r\tWaiting to receive message...')
        elif command == "put":
            ServerPut()
            print('\n\r\tWaiting to receive message...')
        elif command == "list":
            ServerList()
            print('\n\r\tWaiting to receive message...')
        elif command == "exit":
            ServerExit()
        else:
            SendMessageToClient("Unknown input.")
            print('\n\r\tWaiting to receive message...')
    except Exception:
        pass

