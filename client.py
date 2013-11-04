__author__ = 'Jack'

import listener
import os


class Client(listener.Listener):

    def __init__(self, host, port):
        listener.Listener.__init__(self, host, port)
        self.host = host  # Get local machine name
        self.port = port                # Reserve a port for your service.

    def start(self, host, port):
        self.s.start()
        self.s.connect(host, port)

    def upload(self, file_name):
        #s = socket.socket()         # Create a socket object

        #s.connect((self.host, self.port))     # print recieved data

        self.s.send(file_name)
        readByte=open(file_name,"rb")       #read file
        data = readByte.read()
        readByte.close()

        size = os.path.getsize(file_name)   #send the file size(needed for recv())
        self.s.send(str(size))

        self.s.send(data)
        
    def send_message(self, message): 
        #self.s = socket.socket()         # Create a socket object

        #self.s.connect((self.host, self.port))     # print recieved data

        self.s.send(message)

    def on_message(self, addr, data):
        print addr, data

    def stop(self):
        self.s.disconnect()
        self.s.stop()
