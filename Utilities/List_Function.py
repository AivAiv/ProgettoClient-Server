'''
                        LIST
'''

import os

BUFFER_SIZE = 4096
PATH = './Server_Files'
COMMAND = 'list'

# Gets the files from a specified directory
def getFiles():
    # If not present creates the directory
    if not os.path.isdir(PATH):
        os.mkdir(PATH)
    
    file_list = list()
    for entry in os.scandir(PATH):
        if entry.is_file():
            file_list.append(entry.name)
    return file_list

def ListRequest(sock, server_address):
    try:
        # Sends the message to the server
        sock.sendto(COMMAND.encode(), server_address)
        print ('[CLIENT]: LIST command sent to %s' % server_address)
    
        # Gets the answer from the server
        files_list, address = sock.recvfrom(BUFFER_SIZE)
        print('[CLIENT]: Recived files list from %s' % address)
        
        print('\nFiles list:')
        for f in files_list:
            print('>' + f)
        
    except Exception as info:
        print(info)

def ListResponse(sock, client_address):
    #Sends the response
    sock.sendto(getFiles(), client_address)
    print('[SERVER]: Response sent to %s' % client_address)
