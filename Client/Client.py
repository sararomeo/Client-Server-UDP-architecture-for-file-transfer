import socket as sk

# UDP socket creation
sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

# Defining the server address to send messages
server_address = ('localhost', 10000)