import socket as sk
# import time

# UDP socket creation
sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

# associating socket with port

# localhost current IP address (I guess), port 10000 
server_address = ('localhost', 10000)

print ('\n\r starting up on %s port %s' % server_address 'Server socket initialized')
sock.bind(server_address)
print("Successful binding. Waiting for Client now.")




#while True:
#    print('\n\r waiting to receive message...')
#    data, address = sock.recvfrom(4096)

#    print('received %s bytes from %s' % (len(data), address))
#    print (data.decode('utf8'))
    
    
#    if data:
#        data1='Programmazione di Reti'
#        time.sleep(2)
#        sent = sock.sendto(data1.encode(), address)
#        print ('sent %s bytes back to %s' % (sent, address))

