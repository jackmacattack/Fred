from shelvemod import DataFile
from client import *
import server
import time

def on_login_success(c) :
    print 'You have successfully logged in to your OneDir account.'
    start(c)

def on_login_failure(c) :
    print 'Incorrect username or password. Please try again.'
    start(c)

def on_account_created(c) :
    print 'Account created! Please log in to the server now.'
    start(c)

def on_found_password( c, password ) :
    print 'Your password is ' + password
    print 'Please sign in with this information. '
    start(c)

def on_incorrect_found_password(c) :
    print 'Wrong security answer. Please try again. '
    start(c)

def main():

    c = Client("localhost", 12345)

    #time.sleep(2)

    c.start("localhost", 12344)

    #time.sleep(2)

    c.send_message("Connect;localhost;12345")

def start(c) :

    loop = True
    while loop:
        loop = False
        print 'Hello! Welcome to OneDir.'
        print 'If you already have a OneDir account, please enter 1.'
        print 'If you would like to create an account, please enter 2.'
        print 'If you already have an account, but do not remember the password, enter 3.'
        print 'If you don\'t want to use OneDir, enter 0.'
        command = input( "Enter number here: " )

        if command == 1 :
            username = raw_input( 'Username: ')
            password = raw_input( 'Password: ')

            c.send_credentials( username, password )

        elif command == 2 :
            new_username = raw_input( 'What would you like your username to be? ')
            new_password = raw_input( 'What would you like your password to be? ')
            new_password2 = raw_input( 'Please re-enter your password. ' )

            while new_password != new_password2:
                print 'Passwords do not match, please reenter passwords'
                new_password = raw_input( 'Password: ')
                new_password2 = raw_input( 'Re-enter password: ')

            password_question = raw_input( 'Please enter a security question: ')
            password_answer = raw_input( 'Answer to question: ')

            c.create_account( new_username, new_password, password_question, password_answer )

        elif command == 3 :

            find_username = raw_input( 'Please enter your username: ' )
            security_answer = raw_input( 'Please enter your security answer: ' )

            c.forgotten_password( find_username, security_answer )

        elif command == 0 :
            c.stop()

        else:
            loop = True


if __name__ == '__main__':
    main()

