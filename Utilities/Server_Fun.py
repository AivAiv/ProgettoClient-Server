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
    localindex = 0
    while True:
        index, address = sock.recvfrom(BUFFER_SIZE)
        index = index.decode()
        data, address = sock.recvfrom(BUFFER_SIZE)
        if data == b'done':
            print('done receiving file')
            break    
        elif index == str(localindex):
            print('packet and index number received correctly ' + index)
            sentfile += data
            localindex += 1
            sock.sendto('received'.encode(), client_address)
        elif index != str(localindex):
            print('index %s is desynced' + index)
            print('index was %s' % localindex)
            sock.sendto('missing'.encode(), client_address)
            
    print('[SERVER]: Finished reciving data from client (%s, %s)' % address)
    
    try:
        if not os.path.isdir(PATH):
            os.mkdir(PATH)
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

def GetResponse(sock, client_address):
        found = False
        filename, address = sock.recvfrom(BUFFER_SIZE)
        filename = filename.decode()
        for file in getServerFiles():
            if found:
                break
            if file == filename:
                found = True
                print('File ' + filename + ' found!')
                with open('Server_Files/' + filename, 'rb') as f:
                    while True:
                        send = f.read(BUFFER_SIZE)
                        if not send:
                            break
                        sock.sendto(send, client_address)
                sock.sendto('done'.encode(), client_address)
        if not found:  
            print('File ' + filename + ' not found!')
            sock.sendto('notfound'.encode(), client_address)