#!/usr/bin/python3

"""
                                SERVER
"""

import socket as sk
#import threading
from Utilities import Server_Fun as sf

SERVER_ADDRESS = ('localhost', 10000)
BUFFER_SIZE = 4096

sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
sock.bind(SERVER_ADDRESS)
print('Server started and listening on IP: %s and PORT: %s' % SERVER_ADDRESS)

def client_handler(server_socket, client_addr, cmd):
    if cmd == "list":
        sf.ListResponse(server_socket, client_addr)
    
    if cmd == "get":
        sf.GetResponse(server_socket, client_addr)
        
    if cmd == "put":
        sf.PutResponse(server_socket, client_addr)

while True:
    # Listens to requests.
    command, address = sock.recvfrom(BUFFER_SIZE)
    command = command.decode()
    print('\n[SERVER]: Recived %s request from %s' % (command.upper(), address))
    
    if command == "exit":
        sock.sendto('closing'.encode(), address)
        print('[SERVER]: Closing...')
        sock.close()
        break
    else:
        client_handler(sock, address, command)
    
        
    #thread = threading.Thread(target=client_handler, args=(server_socket, cmd, addr))
    #thread.start()
    #thread.join()
