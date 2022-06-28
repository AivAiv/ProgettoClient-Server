'''
                        UDP CLIENT SOCKET
'''

import socket as sk
from Utilities import Input_Translator as it

# Creates UDP socket
sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
server_address = ('localhost', 10000)

# LIST function
def listfun():
    print ('\nlist command!\n')

# GET function
def getfun(file):
    print ('\nget command!\n')

# PUT function
def putfun(file):
    print ('\nput command!\n')

while True:
    
    print ('----------------------\nCommands list:       |')
    print (' - LIST              |')
    print (' - GET <filename>    |')
    print (' - PUT <filename>    |')
    text = input('----------------------\nInsert command: ')
    
    if it.checkInput(text):
        filename, command = it.getInput(text)
    
    while it.checkInput(text) == False:
        text = input('>>> Insert command: ')
        if it.checkInput(text):
            filename, command = it.getInput(text)
    
    if command == 'list':
        listfun()
    elif command == 'get':
        getfun('a')
    elif command == 'put':
        putfun('a')
    elif command == 'exit':
        sock.sendto(text.encode(), server_address)
        sock.close()
        exit()
    else:
        print('yay')
