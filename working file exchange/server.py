'''
                            UDP SERVER SOCKET
'''

import socket as sk
import time

# Creiamo il socket
sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

sentfile = bytearray()
marker = 'empty'

# associamo il socket alla porta
server_address = ('localhost', 10000)
print ('\n\r starting up on %s port %s' % server_address)
sock.bind(server_address)


print('\n\r waiting to receive send marker...')
while True:
    if marker == 'empty':
        marker, address = sock.recvfrom(4096)
        print('Started sending')
    
    if marker.decode() == 'sending':
        data, address = sock.recvfrom(4096)
        if data == b'done':
            marker = 'done'
        else:
            sentfile += data
            #sentfile.append(data)
        
    if marker == 'done':
        print ('done receiving!')
        
        data1='Programmazione di Reti'
        time.sleep(2)
        sent = sock.sendto(data1.encode(), address)
        print ('sent %s bytes back to %s' % (sent, address))
        
        #saves the file
        f = open('Files/dog.jpeg', 'ab')
        f.write(sentfile)
        f.close()
        
        break
    