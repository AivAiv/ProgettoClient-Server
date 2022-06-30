"""
                                CLIENT FUNCTIONS
"""

BUFFER_SIZE = 4096

def ListRequest(sock, server_address):
    try:
        # Sends the message to the server
        sock.sendto('list'.encode(), server_address)
        print ('[CLIENT]: LIST command sent to %s' % server_address)
    
        # Gets the answer from the server
        files_list, address = sock.recvfrom(BUFFER_SIZE)
        print('[CLIENT]: Recived files list from %s' % address)
        
        print('\nFiles list:')
        for f in files_list:
            print('>' + f)
        
    except Exception as info:
        print(info)
        
def PutRequest(sock, server_address, filename):
    try:
       sock.sendto('put'.encode(), server_address)
       sock.sendto(filename.encode(), server_address)
       print('Sending files...')
       with open('Client_Files/' + filename, 'rb') as f:
           while True:
               send = f.read(BUFFER_SIZE)
               if not send:
                   break
               sock.sendto(send, server_address)
       sock.sendto('done'.encode(), server_address)
       msg, server = sock.recvfrom(BUFFER_SIZE)
       print('Done sending files!')
       if msg.decode():
           print('File transfer was successful on ip:' + server)
       else:
           print('File transfer was not completed due to an error. Ip was:' + server)
            
    except Exception as info:
        print(info)