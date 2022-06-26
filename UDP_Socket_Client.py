'''
                        UDP CLIENT SOCKET
'''

import socket as sk
import time


# Create il socket UDP
sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = 'Questo è il corso di ?'

# LIST function
def list():
    print ('list command!')
    return 0

# GET function
def get(file):
    print ('get command!')
    return 1

# PUT function
def put(file):
    print ('put command!')
    return 2

try:

    print ('Commands list:\n- LIST\n- GET <filename>\n- PUT <filename>')
    #command = input('Insert command: ')
    
    # inviate il messaggio
    print ('sending "%s"' % message)
    time.sleep(2) #attende 2 secondi prima di inviare la richiesta
    sent = sock.sendto(message.encode(), server_address)

    # Ricevete la risposta dal server
    print('waiting to receive from')
    data, server = sock.recvfrom(4096)
    #print(server)
    time.sleep(2)
    print ('received message "%s"' % data.decode('utf8'))
except Exception as info:
    print(info)
finally:
    print ('closing socket')
    sock.close()
