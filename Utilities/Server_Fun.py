"""
                                SERVER FUNCTIONS
"""

import os
from Utilities import Input_Translator as it

PATH = './Server_Files'
BUFFER_SIZE = 4096

# Gets the files from a specified directory
def getServerFiles():
    # If not present creates the directory
    if not os.path.isdir(PATH):
        os.mkdir(PATH)
    return it.getFiles(PATH)

def ListResponse(sock, client_address):
    # Sends the response
    for file in getServerFiles():
        sock.sendto(file.encode(), client_address)
    sock.sendto('done'.encode(), client_address)
    print('[SERVER]: Response sent to (%s, %s)' % client_address)
    
def PutResponse(sock, client_address):
    result = 'success'
    
    # Recives the file and saves it in the server's files directory
    filename, address = sock.recvfrom(BUFFER_SIZE)
    filename = filename.decode()
    sentfile = bytearray()
    while True:
        data, address = sock.recvfrom(BUFFER_SIZE)
        if data == b'done':
            break
        else:
            sentfile += data
    print('[SERVER]: Finished reciving data from client (%s, %s)' % address)
    
    try:
        with open('Server_Files/' + filename, 'wb') as f:
            f.write(sentfile)
            f.close()
            print('[SERVER]: File %s --> saved' % filename)
    except:
        result = 'error'
        print('[SERVER]: File %s --> NOT saved' % filename)
    finally:
        
        # Sends the result of the operation
        sock.sendto(result.encode(), client_address)
        print('[SERVER]: Response sent to (%s, %s)' % (client_address))
