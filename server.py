__author__ = 'Jack'

import listener
import os


class Server(listener.Listener):

    def __init__(self, host, port):
        listener.Listener.__init__(self, host, port)
        self.host = host  # Get local machine name
        self.port = port                # Reserve a port for your service.


        self.session = {}

    def start(self):
        self.s.start()

    def add_connection(self, host, port):
        self.s.connect(host, port)

    def saveFile(self, user, path, data):
        folderPath= "\\".join(path.split("\\")[:-1])                #get just folder to check if the folder exists
        folder = os.path.expanduser(".\%s\%s" %(user,folderPath))
        if not os.path.exists(folder):                              #check if folder exists
            os.makedirs(folder)
        fullpath = os.path.expanduser(".\%s\%s" %(user,path))

        createFile = open(fullpath,"wb")
        createFile.write(data)
        createFile.close()

    def auth(self, username, password):
        return True

    def on_message(self, addr, data):
        print addr, data

        arr = data.split(";")
        message = "Love"

        if arr[0] == "Connect":

            self.session[addr[0]] = [arr[1], int(arr[2]), "", "", 0]
            message = "Received"

        elif arr[0] == "Add":
            pass

        elif arr[0] == "Login":

            if self.auth(arr[1], arr[2]):
                self.session[addr[0]][2] = arr[1]
                message = "Success"
            else:
                message = "Failure"

        elif arr[0] == "Message":

            if arr[1] == "Upload":
                self.session[addr[0]][3] = arr[2]
                self.session[addr[0]][4] = int(arr[3])
                message = "File;Send;", arr[2]

        elif arr[0] == "File":

            self.saveFile(self.session[addr[0]][2], self.session[addr[0]][3], data)
            message = "File;Success"

        else:
            pass

        print self.session[addr[0]]
        self.s.connect(self.session[addr[0]][0], self.session[addr[0]][1])
        self.s.send(message)
        self.s.disconnect()

    def stop(self):
        self.s.disconnect()
        self.s.stop()
