'''
                            UDP SERVER SOCKET
'''

import socket as sk
import time
import os
import io
import PIL.Image as Image

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
    
    
    if marker == 'sending':
        data, address = sock.recvfrom(4096)
        if marker != 'done':
            sentfile.append(data)
        
    if marker != 'done':   
        #print('received %s bytes from %s' % (len(data), address))
        print ('done receiving!')
        
        data1='Programmazione di Reti'
        time.sleep(2)
        sent = sock.sendto(data1.encode(), address)
        print ('sent %s bytes back to %s' % (sent, address))
        

        image = open(io.BytesIO(sentfile))
        image.save(os.path.normpath('./Files'))
        
        break
