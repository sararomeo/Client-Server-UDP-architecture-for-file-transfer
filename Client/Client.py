''' 0000969946 sara.romeo3@studio.unibo.it Sara
0000969874 cristina.zoccola@studio.unibo.it Cristina '''
import socket
import sys

sys.path.append('..')
import Commands

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Client socket creation")
    server_address = ('localhost', 10000)
except socket.herror:
    print("Failed to create the client socket")
    sys.exit(-1)

while True:
    try:
        sock.settimeout(None)
        message = input("\nWhat message do you want to send? (get 'file_name', put 'file_name', list, exit): ")
        Commands.SendMessage(message, "server", server_address, sock)

        if "get" in message:
            Commands.ClientGet(sock, message)
        elif "put" in message:
            Commands.ClientPut(message, sock, server_address)
        elif "list" in message:
            Commands.ClientList(sock)
        elif "exit" in message:
            Commands.Exit(sock, "client", "server")
        else:
            print(Commands.ReceiveMessage(sock).decode())
    except TimeoutError:
        pass