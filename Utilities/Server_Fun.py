"""
                                SERVER FUNCTIONS
"""

import os

PATH = './Server_Files'

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

def ListResponse(sock, client_address):
    #Sends the response
    sock.sendto(getFiles(), client_address)
    print('[SERVER]: Response sent to %s' % client_address)
