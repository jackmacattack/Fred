__author__ = 'Jack'

import listener
import os
import changes
import threading
from Tkinter import *
import sys
import gui


class Client(listener.Listener):

    def __init__(self, host, port, parent):
        listener.Listener.__init__(self, host, port)
        self.host = host  # Get local machine name
        self.port = port                # Reserve a port for your service.

        self.gui = gui.Gui(self, parent)

    def start(self, host, port):
        self.s.start()
        self.s.connect(host, port)

    def saveFile(self, path, data):
        '''
        folderPath= "/".join(path.split("/")[:-1])                #get just folder to check if the folder exists
        folder = os.path.expanduser("~/OneDir_server/%s%s" %(user,folderPath))

        print folder

        if not os.path.exists(folder):                              #check if folder exists
            os.makedirs(folder)
        #fullpath = os.path.expanduser("./%s/%s" %(user,path))
        fullpath = folder + "/" + path.split("/")[-1]
        print fullpath
        '''

        createFile = open(fullpath,"wb")
        createFile.write(data)
        createFile.close()

    def remove(self, file_name):
        os.remove(file_name)

    def upload(self, file_name):

        size = os.path.getsize(file_name)   #send the file size(needed for recv())

        message = "Message;Upload;" + file_name + ";" + str(size)

        self.send_message(message)

    def send_file(self, file_name):
        readByte=open(file_name,"rb")       #read file
        data = readByte.read()
        readByte.close()

        self.send_message("File;" + data)

    def send_message(self, message):
        #self.s = socket.socket()         # Create a socket object

        #self.s.connect((self.host, self.port))     # print recieved data
        sys.stdout.flush()
        self.s.send(message)

    def on_message(self, addr, data):
        print "Server to Client:",addr, data

        arr = data.split(";")

        if arr[0] == "Received":
            #where userinput normally starts
            # self.warning.destroy()
            self.gui.on_connect()

        elif arr[0] == "Add":
            if arr[1] == "Success":
                #print out username not accepted please choose a new one
                self.gui.on_add()
            else:
                #normally prints out 'account created'
                self.gui.on_add_fail()

        elif arr[0] == "Login":
            if arr[1] == "Success":
                #normally prints out 'login success'
                self.gui.on_login(arr[2])
            else:
                #normally prints out 'not logged in'
                self.gui.on_login_fail()

        elif arr[0] == "Password":
            #prints out password
            self.gui.print_pass(arr[1])

        elif arr[0] == "File":

            if arr[1] == "Send":
                self.send_file(arr[2])

        elif arr[0] == "Update":

            if arr[1] == "Add":
                self.saveFile(arr[2], arr[3])
            elif arr[1] == "Remove":
                self.remove(arr[2])

    def stop(self):
        self.send_message("Disconnect")
        self.send_message("Debug;Kill")
        self.s.disconnect()
        self.s.stop()
        self.gui.destroy()
        print "Stopping Client"

    def send_credentials(self, user, password) :
        self.send_message("Login;" + user + ";" + password)

    def create_account(self, user, password, q, a) :
        self.send_message("Add;" + user + ";" + password + ";" + q + ";" + a)

    def forgotten_password(self, user, a):
        self.send_message("RecoverPW;" + user + ";" + a)


    #unfinished--------------------------------------------------------------------------------------------------------

    def start_sync(self):
        #need to add watchdog functionality, please leave the boolean
        dir = os.path.expanduser("~/OneDir/")
        handler = changes.TestEventHandler(self, dir)

        self.sync = True

        self.t = threading.Thread(name='listener', target=handler.start)
        self.t.setDaemon(True)
        self.t.start()

        self.t2 = threading.Thread(name='send', target=handler.send_changes)
        self.t2.setDaemon(True)
        self.t2.start()


    def stop_sync(self):
        #need to add watchdog functionality, please leave the boolean
        self.sync = False

    def remove(self, file_name):
        self.send_message("Message;Remove" + file_name)

    def password_change(self, password):
        self.send_message("Message;ChangePW;" + password)

import user_input
