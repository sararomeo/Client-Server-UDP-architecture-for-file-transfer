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



