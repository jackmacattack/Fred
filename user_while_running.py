import user_input
from client import *

def on_logout() :
    print 'You have logged out of OneDir, and your files will no longer sync to the server. '
    user_input.start() #restart the original user interface

def on_sync_off() :
    print 'You are no longer syncing files to the server. To restart the server, enter \'restart\' below.'
    command = input()
    start()

def on_sync_on() :
    print 'You have turned autosync back on. Changes to your directory should appear on the server. '
    start()

def on_password_change( new_password ) :
    print 'You have changed your new password to ' + new_password
    start ()

def start():
    print 'To log out, enter 1. '
    print 'To turn off autosynchronization, enter 2. '
    print 'To turn autosynchronizaiton back on, enter 3. '
    print 'To change your account password, enter 4. '
    command = input( 'Enter number here: ')

    if command == 1 :
        Client.logout() #do we need to ask for username? or can we just shut it down?

    elif command == 2 :
        Client.turn_off()

    elif command == 3 :
        Client.turn_on()

    elif command == 4 :
        Client.change_password()

