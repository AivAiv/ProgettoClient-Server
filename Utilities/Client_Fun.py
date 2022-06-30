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