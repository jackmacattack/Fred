__author__ = 'Jack'

import listener
import os
#import changes
import threading
from Tkinter import *


class Client(listener.Listener):

    def __init__(self, host, port, parent):
        listener.Listener.__init__(self, host, port)
        self.host = host  # Get local machine name
        self.port = port                # Reserve a port for your service.
        self.stop = False

        #GUI
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.f = Frame(parent)
        self.f.pack(padx=15,pady=15)

        # self.warning.pack(side = TOP)

        #Button's wont show until server/client connection is made
        self.log = Button(self.f, text='Log in', command=self.login)
        self.create = Button(self.f, text='Create account', command=self.creation)
        self.forgot = Button(self.f, text='Forgot password', command=self.forgotten)


        #used in login
        #-----------------------------------------------
        self.user_label = Label(self.f, text='Username')
        self.user_entry = Entry(self.f)

        self.pass_label = Label(self.f, text='Password')
        self.pass_entry = Entry(self.f)
        #-----------------------------------------------

        #used in creation
        #-----------------------------------------------
        self.create_user_label = Label(self.f, text='Username')
        self.create_user_entry = Entry(self.f)

        self.create_pass_label = Label(self.f, text='Password')
        self.create_pass_entry = Entry(self.f)

        self.verify_pass_label = Label(self.f, text='Re-enter password')
        self.verify_pass_entry = Entry(self.f)

        self.verify_pass_button = Button(self.f, text='Verify password', command=self.verify_pass)
        #-----------------------------------------------

        #used in verify pass
        #-----------------------------------------------
        self.password_mismatch_label = Label(self.f, text='Passwords do not match, re-enter',foreground='RED')
        self.question_label = Label(self.f, text='Enter security question')
        self.question_entry = Entry(self.f)
        self.answer_label = Label(self.f, text='Answer')
        self.answer_entry = Entry(self.f)
        self.enter_info_button = Button(self.f, text='Enter', command=self.create_account)
        #-----------------------------------------------

        #used in forgotten
        #-----------------------------------------------
        self.forgotten_user_label = Label(self.f, text='Username')
        self.forgotten_user_entry = Entry(self.f)
        self.forgotten_answer_label = Label(self.f, text='Answer to security question')
        self.forgotten_answer_entry = Entry(self.f)
        self.get_password_button = Button(self.f, text='Enter', command=self.forgotten_password)
        self.wrong_security_label = Label(self.f, text='Incorrect answer', foreground='RED')
        #-----------------------------------------------

        self.account_created_label = Label(self.f, text='Account created')
        self.username_unavailable_label = Label(self.f, text='Username unavailable, please try again', foreground='RED')

        self.successful_login_label = Label(self.f, text='Login successful')
        self.unsuccessful_login_label = Label(self.f, text='Login not successful, please try again', foreground='RED')

        self.password_retrieve_label = Label(self.f, text='Your password is: ')

        self.exit = Button(self.f, text="exit", command=self.f.quit)
        # self.exit.pack(side=BOTTOM,padx=10,pady=10)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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
        #print "Server to Client:",addr, data

        arr = data.split(";")

        if arr[0] == "Received":
            #where userinput normally starts
            #user_input.start(self)
            # self.warning.destroy()
            self.log.pack()
            self.create.pack()
            self.forgot.pack()

        elif arr[0] == "Add":
            if arr[1] == "Success":
                #normally prints out 'account created'
                #user_input.on_account_created(self)
                self.account_created_label.pack()
            else:
                #print out username not accepted please choose a new one
                #user_input.on_account_creation_failure(self)
                self.username_unavailable_label.pack()

        elif arr[0] == "Login":
            if arr[1] == "Success":
                #normally prints out 'login success'
                #user_input.on_login_success(self)
                self.successful_login_label.pack()
            else:
                #normally prints out 'not logged in'
                #user_input.on_login_failure(self)
                self.unsuccessful_login_label.pack()

        elif arr[0] == "Password":
                #prints out password
            #user_input.on_found_password(self, arr[1])
            self.password_retrieve_label.pack()

        elif arr[0] == "File":

            if arr[1] == "Send":
                self.send_file(arr[2])

    def stop(self):
        self.s.disconnect()
        self.s.stop()

    def start_sync(self):
        pass
        #self.t = threading.Thread(name='server', target=changes.start(self))
        #t.isDaemon(True)
        #self.t.start()

    def stop_sync(self):
        stop = True

    def logout(self):
        pass

    def password_change(self):
        pass

    def send_credentials(self) :
        self.send_message("Login;" + self.user_entry.get() + ";" + self.pass_entry.get())

    def create_account(self) :
        self.send_message("Add;" + self.create_user_entry.get() + ";" + self.create_pass_entry.get() + ";"
                          + self.question_entry.get() + ";" + self.answer_entry.get())

    def forgotten_password(self):
        self.send_message("RecoverPW;" + self.forgotten_user_entry.get() + ";" + self.forgotten_answer_entry.get())

    def login(self):
        self.log.destroy()
        self.create.destroy()
        self.user_label.pack()
        self.user_entry.pack()
        self.pass_label.pack()
        self.pass_entry.pack()
        self.log = Button(self.f, text='Log in', command=self.send_credentials)
        self.log.pack()
        self.create = Button(self.f, text='Create account', command=self.creation)
        self.create.pack()

    def creation(self):
        # self.log.destroy()
        self.create.destroy()
        self.create_user_label.pack()
        self.create_user_entry.pack()
        self.create_pass_label.pack()
        self.create_pass_entry.pack()
        self.verify_pass_label.pack()
        self.verify_pass_entry.pack()
        self.verify_pass_button.pack()

    def verify_pass(self):
        if self.create_pass_entry.get() != self.verify_pass_entry.get():
            self.password_mismatch_label.pack()

        else:
            self.password_mismatch_label.destroy()
            self.verify_pass_button.destroy()
            self.question_label.pack()
            self.question_entry.pack()
            self.answer_label.pack()
            self.answer_entry.pack()
            self.enter_info_button.pack()

    def forgotten(self):
        self.forgotten_user_label.pack()
        self.forgotten_user_entry.pack()
        self.forgotten_answer_label.pack()
        self.forgotten_answer_entry.pack()
        self.get_password_button.pack()

import user_input
