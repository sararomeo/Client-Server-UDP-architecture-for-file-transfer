import socket as sk
import sys
import os
#import time

BUFFER_SIZE=4096

# UDP datagram socket creation at server's startup
try:    
    sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    # localhost current IP address (I guess), port 10000
    server_address = ('localhost', 10000)
    print ('\n\r starting up on %s port %s' % server_address)
    # port associated to socket
    sock.bind(server_address)
    print("Successful binding. Waiting for Client now.")
    #TODO blocking and timeout
    #sk.setblocking(0)
    #sk.settimeout(15)
except sk.error:
    print("Failed to create socket")
    sys.exit()

def SendMessageToClient(msg):
    msgEn = msg.encode('utf-8')
    sock.sendto(msgEn, clientAddr)
    print ('Sent \"%s\" message to client' % msg)
    
def ReceiveMessageFromClient():
    data, server = sock.recvfrom(BUFFER_SIZE)
    dataDec = data.decode('utf8')
    print(dataDec)

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
    print("List sent from Server")
    ReceiveMessageFromClient()

#if exists, gets file from server dir and sends msg to client, else sends error
def ServerGet(filename):
    SendMessageToClient("Correct command, trying to get your file..")
    if os.path.isfile(filename):
        SendMessageToClient("File exists.")
        #get
        f=open (filename, "rb") 
        data = f.read(1024)
        while (data):
            if(s.sendto(data,clientAddr)):
                print ("sending ...")
                data = f.read(1024)
        f.close()
    else:
        SendMessageToClient("Error: file doesn't exist.")


#La ricezione di un messaggio put contenente il file da caricare sul server e
#l’invio di un messaggio di risposta con l’esito dell’operazion
def ServerPut():
    SendMessageToClient("Correct command, trying to put your file..")
    #TODO put


def ServerExit():
    print("Server socket closed, not sending any message to Client.")
    sock.close()
    sys.exit()

# listening for incoming datagrams
while True:
    print('\n\r Waiting to receive message...')
    data, clientAddr = sock.recvfrom(BUFFER_SIZE)
    text = data.decode('utf8')
    t = text.split()
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
   #non ci arriva     
print("End of communication, closing program.")
quit()
