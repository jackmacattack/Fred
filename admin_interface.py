__author__ = 'msstudent'

def main() :
    print 'This is the admin interface of OneDir. Please sign in using your admin username and password.'
    username = raw_input( 'Username: ')
    password = raw_input( 'Password: ')
    #if the username and password link to an admin account, print the rest
    print 'Please enter the number of the command you would like to execute.'
    print '1. View a users profile information.'
    print '2. Look at a list of all the users files in their directory.'
    print '3. Remove a user and their entire directory.'
    print '4. Remove a specific file from a users directory.'
    print '5. View the total size of a users directory.'
    print '6. Examine the size of a specific file in a users directory.'
    print '7. Get the total size of all the files on OneDir.'
    print '8. View the history of connections to the OneDir server.'
    print '9. Reset a users password.'
    #other possible commands: restart server, move files, connect accounts/merge directories

    command = input( "Command: " )

    if command == 1 :
        user = raw_input( 'Username of the desired profile: ')
        #return the username and profile and all other information from the flat file
    if command == 2 :
        user = raw_input( 'Username of the desired profile: ')
        #return the list of all the the directory
    if command == 3 :
        user = raw_input( 'Username of the user you would like to remove: ')
        #return true if the user was removed
        print 'User was removed succesfully.'
    if command == 4 :
        user = raw_input( 'Username of the desired profile: ')
        filename = raw_input( 'File to remove: ')
        #find that user and file and remove it from server (maybe client?)
    if command == 5 :
        user = raw_input( 'Username of the desired profile: ')
        #return size of directory
    if command == 6 :
        user = raw_input( 'Username of the desired profile: ')
        filename = raw_input( 'Filename: ')
    if command == 7 :
        #return whole OneDir size
        print 'Size: '
    if command == 8 :
        #rerturn all the connection times and users - whatever is possible here
        print 'Times: '
    if command == 9 :
        user = raw_input( 'Username that requires a new password: ')
        password = raw_input( 'Enter the new password for this user: ')

if __name__ == '__main__' :
    main()
