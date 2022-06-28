'''
                        UDP CLIENT SOCKET
'''

import socket as sk
import time
from Utilities import Input_Translator as it

BUFFER_SIZE = 4096

# Create il socket UDP
sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

server_address = ('localhost', 10000)
filename = "Esempio Powerpoint.pptx"
message = open("Client_Files/dog.jpeg", "rb")

# LIST function
def lists():
    print('Files list:')
    for f in it.getFiles():
        print(f)

# GET function
def gets(file):
    print ('get command!')
    return 1

# PUT function
def puts(file):
    print ('put command!')
    return 2

try:
    print ('Commands list:\n- LIST\n- GET <filename>\n- PUT <filename>')
    inp = input('Insert command: ')
    
    filename, command = it.checkInput(inp);
    
    while (filename == '1') or (filename == '2'):
        print("not funny!")
        filename, command = it.checkInput(inp);
    
    if command == 'list':
        lists()
    if command == 'get':
        gets('a')
    if command == 'put':
        puts('a')
    
    # inviate il messaggio
    print ('sending "%s"' % message)
    time.sleep(2) #attende 2 secondi prima di inviare la richiesta
    #sent = sock.sendto(message, server_address)
    
    
    sock.sendto('sending'.encode(), server_address)
    sock.sendto(filename.encode(), server_address)
    with open('Client_Files/' + filename, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            sock.sendto(bytes_read, server_address)
            #print ('sending byte packet "%s"' % bytes_read)
    sock.sendto('done'.encode(), server_address) 



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