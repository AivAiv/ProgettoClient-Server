"""
                                CLIENT FUNCTIONS
"""

BUFFER_SIZE = 4096

def ListRequest(sock, server_address):
    try:
        # Sends the command to the server
        sock.sendto('list'.encode(), server_address)
        print ('[CLIENT]: LIST command sent to (%s, %s)' % server_address)
    
        # Gets the answer from the server
        files_list = list()
        file = ''
        while file != 'done':
            file, address = sock.recvfrom(BUFFER_SIZE)
            file = file.decode('utf-8')
            files_list.append(file)
        files_list.remove('done')
        print('[CLIENT]: Recived files list from (%s, %s)' % address)
        
        print('\nServer files list:')
        for f in files_list:
            print(' > ' + f)
        
    except Exception as info:
        print(info)
        
def PutRequest(sock, server_address, filename):
    try:
        # Sends command and file to the server
       sock.sendto('put'.encode(), server_address)
       sock.sendto(filename.encode(), server_address)
       print('[CLIENT]: Sending files...')
       with open('Client_Files/' + filename, 'rb') as f:
           while True:
               send = f.read(BUFFER_SIZE)
               if not send:
                   break
               sock.sendto(send, server_address)
       sock.sendto('done'.encode(), server_address)
       
       # Waits for server's response
       msg, server = sock.recvfrom(BUFFER_SIZE)
       print('[CLIENT]: Server (%s, %s) finished sending files!' % server)
       if msg.decode('utf-8') == 'success':
           print('[CLIENT]: File transfer was successful on ip: %s, %s' % server)
       else:
           print('[CLIENT]: File transfer was not completed due to an error. Ip was: %s, %s' % server)
            
    except Exception as info:
        print(info)

def GetRequest(sock, server_address, filename):
     # Sends command and file to the server
    sock.sendto('get'.encode(), server_address)
    sock.sendto(filename.encode(), server_address)
    print('[CLIENT]: Waiting for files...')

    sentfile = bytearray()
    while True:
        data, address = sock.recvfrom(BUFFER_SIZE)
        if data == b'done':
            break
        elif data == b'notfound':
            print('[CLIENT]: File is not present on server')
            break
        else:
            sentfile += data
    
    
    if data == b'done':
        print('[CLIENT]: Finished reciving data from server (%s, %s)' % address)
        try:
            with open('Client_Files/' + filename, 'wb') as f:
                f.write(sentfile)
                f.close()
                print('[CLIENT]: File %s --> saved' % filename)
        except:
            print('[CLIENT]: File %s --> NOT saved' % filename)