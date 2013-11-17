from shelvemod import DataFile
import client

d = DataFile("test.txt")

def on_login_success() :
    print 'You have successfully logged in to your OneDir account.'

def on_login_failure() :
    print 'Incorrect username or password. Please try again.'
    main()

def on_account_created() :
    print 'Account created! Please log in to the server now.'
    main()

def on_found_password( password ) :
    print 'Your password is ' + password
    print 'Please sign in with this information. '
    main()

def on_incorrect_found_password( ) :
    print 'Wrong security answer. Please try again. '
    main()


def main() :
    print 'Hello! Welcome to OneDir.'
    print 'If you already have a OneDir account, please enter 1.'
    print 'If you would like to create an account, please enter 2.'
    print 'If you already have an account, but do not remember the password, enter 3.'
    print 'If you are an admin, please enter 4.'
    print 'If you dont want to use OneDir, enter 0.'
    command = input( "Enter number here: " )

    if command == 1 :
        username = raw_input( 'Username: ')
        password = raw_input( 'Password: ')

        client.send_credentials( username, password )

    if command == 2 :
        new_username = raw_input( 'What would you like your username to be? ')
        new_password = raw_input( 'What would you like your password to be? ')
        new_password2 = raw_input( 'Please re-enter your password. ' )

        while new_password != new_password2:
            print 'Passwords do not match, please reenter passwords'
            new_password = raw_input( 'Password: ')
            new_password2 = raw_input( 'Re-enter password: ')

        password_question = raw_input( 'Please enter a security question: ')
        password_answer = raw_input( 'Answer to question: ')

        client.create_account( new_username, new_password, password_question, password_answer )

    if command == 3 :

        find_username = raw_input( 'Please enter your username: ' )
        security_answer = raw_input( 'Please enter your security answer: ' )

        client.forgotten_password( find_username, security_answer )

