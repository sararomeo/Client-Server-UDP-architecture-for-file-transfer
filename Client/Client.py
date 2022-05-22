import socket as sk
import sys

try:
    # UDP socket creation
    sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    print("Client socket creation")
    # Defining the server address to send messages
    server_address = ('localhost', 10000)
except sk.error:
    print("Failed to create the client socket")
    sys.exit()
    
msg = input("What message do you want to send? (get 'file_name', put 'file_name', list, exit): ")

def SendMessage(message):
    messageEncoded = message.encode('utf_8')
    sk.sendto(messageEncoded, server_address)
    print("Sending %s message to server" % msg)