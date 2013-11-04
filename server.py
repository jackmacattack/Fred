__author__ = 'Jack'

import listener
import os


class Server(listener.Listener):

    def __init__(self):
        pass

    def saveFile(self, user, path, data):
        folderPath= "\\".join(path.split("\\")[:-1])                #get just folder to check if the folder exists
        folder = os.path.expanduser(".\%s\%s" %(user,folderPath))
        if not os.path.exists(folder):                              #check if folder exists
            os.makedirs(folder)
        fullpath = os.path.expanduser(".\%s\%s" %(user,path))

        createFile = open(fullpath,"wb")
        createFile.write(data)
        createFile.close()
