'''
                        INPUT TRANSLATOR
'''
import os

PATH = 'Client_Files/'
err_file = 0

# Retrieves the files from 'PATH' directory.
def getFiles(path):
    fileList = list()
    for entry in os.scandir(path):
        if entry.is_file():
            fileList.append(entry.name)
    return fileList

# Splits the input string.
def split(inString):
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

# Checks if the given input suits the requirements.
def checkInput(inString):
    global err_file
    fileName = 'empty'
    if len(inString) > 0:
        if inString.startswith(' '):
            err_file = 0
            return False
        
        # Separates the command and the file name.
        fileName, command = split(inString)
        
        # Checks if the command is valid.
        if not (command == 'put' or command == 'get' or command == 'list' or command == 'exit'):
            err_file = 0
            return False
        
        # Checks if the file name is valid.
        found = False
        for name in getFiles(PATH):
            if fileName == name:
                found = True
            
        if command == 'list' or command == 'exit':
            found = True
        
        if not found:
            err_file = 1
            return False
        
        return True

def getInput(inString):
    global err_file
    fileName = ''
    command = 'empty'
    
    if checkInput(inString):
        return split(inString)
    else:
        if err_file == 1:
            fileName = '[File not found]'
            command = 'empty'
        else:
            fileName = 'empty'
            command = '[Unknown command]'
        return fileName, command
