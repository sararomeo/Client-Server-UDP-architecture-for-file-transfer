import socket as sk
import sys
#import time

# UDP socket creation
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

# creates a list with all available file
def ServerList():
    print("Trying to get available files list..")
    
#L’invio del messaggio di risposta al comando get contenente il file richiesto,
# se presente, od un opportuno messaggio di errore;
def ServerGet():
    print("Trying to get your file..")

#La ricezione di un messaggio put contenente il file da caricare sul server e
#l’invio di un messaggio di risposta con l’esito dell’operazion
def ServerPut():
    print("Trying to put your file..")

def ServerExit():
    print("Server socket closed, not sending any message to Client.")
    sk.close()
    sys.exit()

# "main"
while True:
    print('\n\r Waiting to receive message...')
    data, clientAddr = sk.recvfrom(4096)
    text = data.decode('utf8')
    t = text.split()
    #TODO : fix Invalid syntax (pyflakes E) error 
    match t[0]:
        case "get":
            print("Going to get your file..")
            ServerGet()
        case "put":
            print("Going to put your file..")
            ServerPut()
        case "list":
            print("Going to get available files list..")
            ServerList()
        case "exit":
            ServerExit()
        case _:
            print("Unknown input.")
            
print("End of communication, closing program.")
quit()

