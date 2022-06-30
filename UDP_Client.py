#!/usr/bin/python3

"""
                                CLIENT
"""

import socket as sk
from Utilities import Input_Translator as it

SERVER_ADDRESS = ('localhost', 10000)
BUFFER_SIZE = 4096

sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
print('Client connected to IP: %s and PORT: %s\n' % SERVER_ADDRESS)

while True:
    print ('----------------------\nCommands list:       |')
    print (' - LIST              |')
    print (' - GET <filename>    |')
    print (' - PUT <filename>    |')
    text = input('----------------------\nInsert command: ')
    
    # Checks input correctness.
    if it.checkInput(text):
        filename, command = it.getInput(text)
    
    while it.checkInput(text) == False:
        text = input('>>> Insert command: ')
        if it.checkInput(text):
            filename, command = it.getInput(text)
    
    # Manages commands.
    if command == 'list':
        listfun()
    
    if command == 'get':
        getfun('a')
    
    if command == 'put':
        putfun('a')
    
    if command == 'exit':
        sock.sendto(text.encode(), SERVER_ADDRESS)
        sock.close()
        exit()
