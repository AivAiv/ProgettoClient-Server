#!/usr/bin/python3

"""
                                SERVER
"""

import socket as sk
#import threading

SERVER_ADDRESS = ('localhost', 10000)
BUFFER_SIZE = 4096

sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
sock.bind(SERVER_ADDRESS)
print('Server started and listening on IP: %s and PORT: %s\n' % SERVER_ADDRESS)

def client_handler(server_socket, client_addr, cmd, filename):
    if cmd == "list":
        print()
        #list_files(server_socket, addr)
    if cmd == "get":
        print()
        #send_file(server_socket, filename, addr)
    if cmd == "put":
        print()
        #update_file(server_socket, filename, addr)

while True:
    # Listens to requests.
    command, address = sock.recvfrom(BUFFER_SIZE)
    print('[SERVER]: Recived %s request from %s' % (command, address))
    command = command.decode('utf-8')
    
    if command == "exit":
        sock.close()
        exit()
    else:
        client_handler(sock, address, command)
    
        
    #thread = threading.Thread(target=client_handler, args=(server_socket, cmd, addr))
    #thread.start()
    #thread.join()
