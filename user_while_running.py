import user_input
from client import *

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

