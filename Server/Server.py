''' 0000969946 sara.romeo3@studio.unibo.it Sara
0000969874 cristina.zoccola@studio.unibo.it Cristina '''
import socket
import sys

sys.path.append('..')
import Commands

try:    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 10000)
    print (f"\n\r starting up on {server_address[0]} port {server_address[1]}")
    sock.bind(server_address)
    print("Successful binding. Waiting for Client now.")
except socket.herror:
    print("Failed to create socket")
    sys.exit(-1)

while True:
    try:
        sock.settimeout(None)
        print('\n\r Waiting to receive message...')
        data, clientAddr = sock.recvfrom(4096)
        t = data.decode().split(' ', 1)
        command = t[0]

        if command == "get":
            Commands.ServerGet(t[1], sock, clientAddr)
        elif command == "put":
            Commands.ServerPut(t[1], clientAddr, sock)
        elif command == "list":
            Commands.ServerList(sock, clientAddr)
        elif command == "exit":
            Commands.Exit(sock, "server", "client")
        else:
            Commands.SendMessage("Unknown input.", "client", clientAddr, sock)
    except TimeoutError:
        pass