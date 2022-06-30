"""
                                SERVER FUNCTIONS
"""

import os

PATH = './Server_Files'
BUFFER_SIZE = 4096

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
    
def PutResponse(sock, client_address):
    result = 'success'
    filename, address = sock.recvfrom(BUFFER_SIZE)
    filename = filename.decode()
    sentfile = bytearray()
    while True:
        data, address = sock.recvfrom(BUFFER_SIZE)
        if data == b'done':
            break
        else:
            sentfile += data
    
    try:
        with open('Server_Files/' + filename, 'wb') as f:
            f.write(sentfile)
            f.close()      
    except:
        result = 'error'
    finally:      
        sock.sendto(result.encode(), client_address)
        
        
        
    
