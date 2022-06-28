import socket 
import os

BUFFER_SIZE = 4096

def listCommand(sock, server_address):
    print()

def getCommand(sock, server_address, filename):
    print()

def putCommand(sock, server_address, filename):
    try:
        # Sends the message
        sock.sendto('put'.encode(), server_address)
        #sock.sendto('sending'.encode(), server_address)
        sock.sendto(filename.encode(), server_address)
        with open(filename, "rb") as f:
            while True:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break
                sock.sendto(bytes_read, server_address)
        sock.sendto('done'.encode(), server_address) 
    
        # Recive the answer
        data, server = sock.recvfrom(4096)
        print ('received message "%s"' % data.decode('utf8'))
    except Exception as info:
        print(info)
    finally:
        print ('closing socket')
        sock.close()
    
def end_process(socket, server_address, op):
    socket.sendto(op.encode(), server_address)
    socket.close()
    print('\nExiting...')
    exit()