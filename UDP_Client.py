#!/usr/bin/python3

"""
                                CLIENT
"""

import socket as sk
from Utilities import Input_Translator as it
from Utilities import Client_Fun as cf

SERVER_ADDRESS = ('localhost', 10000)
BUFFER_SIZE = 4096

sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
print('Client connected to IP: %s and PORT: %s' % SERVER_ADDRESS)

def check(string):
    print(string)
    text = input('>>> Insert command: ')
    filename, command = it.getInput(text)
    return text, filename, command
    

while True:
    print ('\n----------------------\nCommands list:       |')
    print (' - LIST              |')
    print (' - GET <filename>    |')
    print (' - PUT <filename>    |')
    print (' - EXIT              |')
    text = input('----------------------\nInsert command: ')
    
    # Checks input correctness.
    filename, command = it.getInput(text)
    
    while it.checkInput(text) == False:
        if command == 'empty':
            text, filename, command = check(filename)
        else:
            text, filename, command = check(command)
    
    # Manages commands.
    if command == 'list':
        cf.ListRequest(sock, SERVER_ADDRESS)
    
    if command == 'get':
        print()
        #getfun('a')
    
    if command == 'put':
        cf.PutRequest(sock, SERVER_ADDRESS, filename)
    
    if command == 'exit':
        sock.sendto(command.encode(), SERVER_ADDRESS)
        msg, address = sock.recvfrom(BUFFER_SIZE)
        print('\n[CLIENT]: Closing...')
        sock.close()
        break
