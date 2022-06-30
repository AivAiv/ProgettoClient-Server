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
print('Client connected to IP: %s and PORT: %s\n' % SERVER_ADDRESS)

while True:
    print ('----------------------\nCommands list:       |')
    print (' - LIST              |')
    print (' - GET <filename>    |')
    print (' - PUT <filename>    |')
    """
    text = input('----------------------\nInsert command: ')
    
    # Checks input correctness.
    if it.checkInput(text):
        filename, command = it.getInput(text)
    
    while it.checkInput(text) == False:
        text = input('>>> Insert command: ')
        if it.checkInput(text):
            filename, command = it.getInput(text)
    """
    command = 'put'
    filename = 'Document.docx'
    text = ''
    
    # Manages commands.
    if command == 'list':
        cf.ListRequest(sock, SERVER_ADDRESS)
    
    if command == 'get':
        print()
        #getfun('a')
    
    if command == 'put':
        cf.PutRequest(sock, SERVER_ADDRESS, filename)
    
    if command == 'exit':
        sock.sendto(text.encode(), SERVER_ADDRESS)
        sock.close()
        exit()
