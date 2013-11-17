__author__ = 'Jack'

import listener
import os
import user_input


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

        size = os.path.getsize(file_name)   #send the file size(needed for recv())

        self.s.send("Message;Upload;", file_name, ";", str(size))

    def send_file(self, file_name):
        readByte=open(file_name,"rb")       #read file
        data = readByte.read()
        readByte.close()

        self.s.send("File;", data)
        
    def send_message(self, message): 
        #self.s = socket.socket()         # Create a socket object

        #self.s.connect((self.host, self.port))     # print recieved data

        self.s.send(message)

    def on_message(self, addr, data):
        print addr, data

        arr = data.split(":")

        if arr[0] == "Received":
            pass

        elif arr[0] == "UserAdd":
            pass

        elif arr[0] == "File":

            if arr[1] == "Send":
                self.send_file(arr[2])

    def stop(self):
        self.s.disconnect()
        self.s.stop()
        
    def send_credentials(self, username, password) :
        self.send_message("Login;", username, ";", password)

    def create_account(self, new_username, new_password, password_question, password_answer ) :
        self.send_message("Add;", new_username, ";", new_password, ";", password_question, ";", password_answer)

    def forgotten_password_check(self, username, answer ):
        self.send_message("RecoverPW;", username, ";", answer)
