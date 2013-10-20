
def main() :
    print 'Hello! Welcome to OneDir.'
    print 'If you already have a OneDir account, please enter 1.'
    print 'If you would like to create an account, please enter 2.'
    #don't know if we want this or not
    print 'If you already have an account, but do not remember the password, enter 3.'
    print 'If you dont want to use OneDir, enter 0.'
    command = input( "Enter number here: " )

    if command == 1 :
        username = raw_input( 'Username: ') #hey
        password = raw_input( 'Password: ')
        #search on database to find that username and password pair
        #return true or false
    if command == 2 :
        new_username = raw_input( 'What would you like your username to be? ')
        new_password = raw_input( 'What would you like your new password to be? ')
        new_password2 = raw_input( 'Please re-enter your new password. ')
        if new_password == new_password2 :
            #set username and password on database
            print 'Account successfully created for ' + new_username + '!'
    #if we decide to use this feature
    if command == 3 :
        find_username = raw_input( 'Please enter your username: ' )
        #search database for username...print password?
    if command == 0 :
        print 'Goodbye!'


if __name__ == '__main__' :
    main()
