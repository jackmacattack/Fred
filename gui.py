__author__ = 'Jack'

import listener
import os
import changes
import threading
from Tkinter import *
import sys


class Gui():

    def __init__(self, c, parent):

        #GUI
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.f = Frame(parent)
        self.f.pack(padx=15,pady=15)

        # self.warning.pack(side = TOP)

        #Button's wont show until server/client connection is made
        self.log = Button(self.f, text='Log in', command=self.login)
        self.create = Button(self.f, text='Create account', command=self.creation)
        self.forgot = Button(self.f, text='Forgot password', command=self.forgotten)

        #Home button
        self.home = Button(self.f, text='Home', command=self.home)


        #used in login
        self.user_label = Label(self.f, text='Username')
        self.user_entry = Entry(self.f)

        self.pass_label = Label(self.f, text='Password')
        self.pass_entry = Entry(self.f)


        #used in creation
        self.create_user_label = Label(self.f, text='Username')
        self.create_user_entry = Entry(self.f)

        self.create_pass_label = Label(self.f, text='Password')
        self.create_pass_entry = Entry(self.f)

        self.verify_pass_label = Label(self.f, text='Re-enter password')
        self.verify_pass_entry = Entry(self.f)

        self.verify_pass_button = Button(self.f, text='Verify password', command=self.verify_pass)


        #used in verify pass
        self.password_mismatch_label = Label(self.f, text='Passwords do not match, re-enter',foreground='RED')
        self.question_label = Label(self.f, text='Enter security question')
        self.question_entry = Entry(self.f)
        self.answer_label = Label(self.f, text='Answer')
        self.answer_entry = Entry(self.f)
        self.enter_info_button = Button(self.f, text='Enter', command=self.create_account)


        #used in forgotten
        self.forgotten_user_label = Label(self.f, text='Username')
        self.forgotten_user_entry = Entry(self.f)
        self.forgotten_answer_label = Label(self.f, text='Answer to security question')
        self.forgotten_answer_entry = Entry(self.f)
        self.get_password_button = Button(self.f, text='Enter', command=self.forgotten_password)
        self.wrong_security_label = Label(self.f, text='Incorrect answer', foreground='RED')


        #used for account creation stuff
        self.account_created_label = Label(self.f, text='Account created')
        self.username_unavailable_label = Label(self.f, text='Username unavailable, please try again', foreground='RED')


        #used if successful login
        self.welcome_label = Label(self.f, text='Welcome, ' + self.user_entry.get() +'!')
        self.sync_on_button = Button(self.f, text='Turn sync on', command=c.start_sync)
        self.sync_off_button = Button(self.f, text='Turn sync off', command=c.stop_sync)
        self.sync = False
        self.logout_button = Button(self.f, text='Log out', command=self.logout)
        self.change_password_button = Button(self.f, text='Change password', command=self.change)
        self.change_password_entry_1 = Entry(self.f)

        #used if user is changing password
        self.change_password_label_1 = Label(self.f, text='New password')
        self.change_password_entry_2 = Entry(self.f)
        self.change_password_label_2 = Label(self.f, text='Re-enter password')
        self.check_password_button = Button(self.f, text='Verify password', command=self.password_change)
        self.password_change_label = Label(self.f, text='Password changed!', foreground='RED')
        self.login_home_button = Button(self.f, text='Home', command = self.login_home)


        #unsuccessful login attempt
        self.unsuccessful_login_label = Label(self.f, text='Login not successful, please try again', foreground='RED')

        #used if security question answer is correct
        self.password_retrieve_label = Label(self.f, text='Your password is: ')

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        self.c = c
        self.root = parent

    def on_connect(self):
        #where userinput normally starts
        # self.warning.destroy()
        self.log.pack()
        self.create.pack()
        self.forgot.pack()

    def on_add(self):
        #print out username not accepted please choose a new one
        self.account_created_label.pack()
        self.username_unavailable_label.forget()

    def on_add_fail(self):
        #normally prints out 'account created'
        self.account_created_label.forget()
        self.username_unavailable_label.pack()

    def on_login(self, user):
        self.welcome_label = Label(self.f, text='Welcome, ' + user + '!')
        self.welcome_label.pack(side=TOP)
        self.unsuccessful_login_label.forget()
        self.forget_login()
        self.log.forget()
        self.sync_on_button.pack()
        self.sync_off_button.pack()
        self.home.forget()
        self.change_password_button.pack()
        self.logout_button.pack(side=BOTTOM,padx=10,pady=10)

    def on_login_fail(self):
        self.unsuccessful_login_label.pack(side=TOP)

    def print_pass(self, password):
        self.password_retrieve_label = Label(self.f, text='Your password is: ' + password)
        self.password_retrieve_label.pack()

    def destroy(self):
        self.root.destroy()
        self.root.quit()

    def change(self):
        #used when user is logged in and changing their password
        self.welcome_label.forget()
        self.sync_off_button.forget()
        self.sync_on_button.forget()
        self.logout_button.forget()
        self.change_password_button.forget()
        self.change_password_label_1.pack()
        self.change_password_entry_1.pack()
        self.change_password_label_2.pack()
        self.change_password_entry_2.pack()
        self.check_password_button.pack()
        self.login_home_button.pack(padx=10,pady=10)


    def login_home(self):
        #home button for when a user is logged in succesfully
        self.password_change_label.forget()
        self.password_mismatch_label.forget()
        self.change_password_entry_1.forget()
        self.change_password_entry_2.forget()
        self.change_password_label_1.forget()
        self.change_password_label_2.forget()
        self.change_password_entry_2.delete(0, END)
        self.change_password_entry_1.delete(0, END)

        self.welcome_label.pack()
        self.sync_on_button.pack()
        self.sync_off_button.pack()
        self.change_password_button.pack()
        self.login_home_button.forget()
        self.check_password_button.forget()
        self.logout_button.pack(side=BOTTOM,padx=10,pady=10)

    def send_credentials(self) :
        self.c.send_credentials(self.user_entry.get(), self.pass_entry.get())

    def create_account(self) :
        self.c.create_account(self.create_user_entry.get(), self.create_pass_entry.get(), 
                            self.question_entry.get(), self.answer_entry.get())

    def forgotten_password(self):
        self.c.forgotten_password(self.forgotten_user_entry.get(), self.forgotten_answer_entry.get())

    def login(self):
        #log's user in
        self.log.forget()
        self.create.forget()
        self.forgot.forget()

        self.forget_create()

        self.forget_forgot()

        self.user_label.pack()
        self.user_entry.pack()
        self.pass_label.pack()
        self.pass_entry.pack()
        self.log = Button(self.f, text='Log in', command=self.send_credentials)
        self.log.pack()
        self.home.pack(side=BOTTOM, padx=10,pady=10)

    def creation(self):
        #creates user
        self.forget_login()

        self.forget_forgot()

        self.create.forget()
        self.log.forget()
        self.forgot.forget()

        self.create_user_label.pack()
        self.create_user_entry.pack()
        self.create_pass_label.pack()
        self.create_pass_entry.pack()
        self.verify_pass_label.pack()
        self.verify_pass_entry.pack()
        self.verify_pass_button.pack()

        self.home.pack(side=BOTTOM, padx=10,pady=10)

    def verify_pass(self):
        #checks if passwords match when creating account
        if self.create_pass_entry.get() != self.verify_pass_entry.get():
            self.password_mismatch_label.pack()

        else:
            self.password_mismatch_label.forget()
            self.verify_pass_button.forget()
            self.question_label.pack()
            self.question_entry.pack()
            self.answer_label.pack()
            self.answer_entry.pack()
            self.enter_info_button.pack()

    def forgotten(self):
        #used when someone forgets their password
        self.forget_create()

        self.forget_login()

        self.log.forget()
        self.create.forget()
        self.forgot.forget()

        self.forgotten_user_label.pack()
        self.forgotten_user_entry.pack()
        self.forgotten_answer_label.pack()
        self.forgotten_answer_entry.pack()
        self.get_password_button.pack()

        self.home.pack(side=BOTTOM, padx=10,pady=10)

    def forget_login(self):
        #used to refresh frame of login junk
        self.user_label.forget()
        self.user_entry.forget()
        self.pass_label.forget()
        self.pass_entry.forget()

    def forget_forgot(self):
        #used to refresh frame of forgotten password junk
        self.forgotten_user_entry.forget()
        self.forgotten_answer_entry.forget()
        self.forgotten_user_label.forget()
        self.forgotten_answer_label.forget()
        self.get_password_button.forget()


    def forget_create(self):
        #used to refresh frame of creating account junk
        self.create_user_entry.forget()
        self.create_user_label.forget()
        self.create_pass_entry.forget()
        self.create_pass_label.forget()
        self.account_created_label.forget()
        self.username_unavailable_label.forget()
        self.verify_pass_button.forget()
        self.verify_pass_entry.forget()
        self.verify_pass_label.forget()
        self.question_entry.forget()
        self.question_label.forget()
        self.answer_entry.forget()
        self.answer_label.forget()
        self.enter_info_button.forget()

    def home(self):
        #used to get back to the first frame
        self.forget_create()
        self.forget_login()
        self.forget_forgot()
        self.log.forget()
        self.create.forget()
        self.forgot.forget()
        self.password_retrieve_label.forget()

        self.refresh_create_entries()
        self.refresh_forget_entries()
        self.refresh_login_entries()

        self.welcome_label.forget()

        self.sync_on_button.forget()
        self.sync_off_button.forget()

        self.log = Button(self.f, text='Log in', command=self.login)
        self.create = Button(self.f, text='Create account', command=self.creation)
        self.forgot = Button(self.f, text='Forgot password', command=self.forgotten)

        self.log.pack()
        self.create.pack()
        self.forgot.pack()
        self.home.forget()
        self.logout_button.forget()
        self.unsuccessful_login_label.forget()

    def refresh_login_entries(self):
        #clears login entries
        self.user_entry.delete(0, END)
        self.pass_entry.delete(0, END)

    def refresh_create_entries(self):
        #clears creation entries
        self.create_user_entry.delete(0, END)
        self.create_pass_entry.delete(0, END)
        self.verify_pass_entry.delete(0, END)
        self.question_entry.delete(0, END)
        self.answer_entry.delete(0, END)

    def refresh_forget_entries(self):
        #clears forgotten entries
        self.forgotten_user_entry.delete(0, END)
        self.forgotten_answer_entry.delete(0, END)


    #unfinished--------------------------------------------------------------------------------------------------------

    def logout(self):
        #as of right now this just turns calls stop_sync and refreshed all the entries and goes to the home menu,
        #completely finished if you do not want to add anything else

        self.c.stop_sync()
        self.forget_create()
        self.forget_login()
        self.forget_forgot()
        self.log.forget()
        self.create.forget()
        self.forgot.forget()

        self.refresh_create_entries()
        self.refresh_forget_entries()
        self.refresh_login_entries()

        self.welcome_label.forget()

        self.sync_on_button.forget()
        self.sync_off_button.forget()

        self.log = Button(self.f, text='Log in', command=self.login)
        self.create = Button(self.f, text='Create account', command=self.creation)
        self.forgot = Button(self.f, text='Forgot password', command=self.forgotten)

        self.log.pack()
        self.create.pack()
        self.forgot.pack()
        self.home.forget()
        self.logout_button.forget()
        self.unsuccessful_login_label.forget()
        self.change_password_button.forget()

    def password_change(self):
        #jack, you need to send the take self.change_password_entry_1.get() and set it as the users new password
        if self.change_password_entry_1.get() == self.change_password_entry_2.get():
            self.password_mismatch_label.forget()
            self.password_change_label.pack()
            self.c.password_change(self.change_password_entry_1.get())
        else:
            self.password_mismatch_label.pack()

import user_input
