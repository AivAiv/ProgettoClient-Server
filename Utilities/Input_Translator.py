'''
                        INPUT TRANSLATOR
'''
import os

PATH = 'Client_Files/'
uno = 1
due = 2

# Retrieves the files from Files directory.
def getFiles():
    fileList = list()
    for entry in os.scandir(PATH):
        if entry.is_file():
            fileList.append(entry.name)
    return fileList

# Checks if the given input suits the requirements.
def checkInput(inString):
    fileName = 'empty'
    if len(inString) > 0:
        if inString.startswith(' '):
            return False
        
        # Splits the input string.
        splittedString = inString.split()
        
        # Separates the command.
        command = splittedString[0].lower()
        
        # Separates the file name.
        for x in splittedString:
            if x != splittedString[0]:
                if x == splittedString[1]:
                    fileName = x
                else:
                    fileName += ' ' + x
        
        # Checks if the command is valid.
        if not (command == 'put' or command == 'get' or command == 'list' or command == 'exit'):
            print('[Unknown command]')
            return False
        
        # Checks if the file name is valid.
        found = False
        
        for name in getFiles():
            if fileName == name:
                found = True
            
        if command == 'list' or command == 'exit':
            found = True
        
        if not found:
            print('[File not founded]')
            return False
        
        return True

def getInput(inString):
    fileName = ''
    splittedString = inString.split()
    command = splittedString[0].lower()
    for x in splittedString:
        if x != splittedString[0]:
            if x == splittedString[1]:
                fileName = x
            else:
                fileName += ' ' + x
    return fileName, command
