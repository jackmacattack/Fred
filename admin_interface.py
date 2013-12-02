__author__ = 'msstudent'
from shelvemod import DataFile
import server
import os
d = DataFile('test.txt')

def on_log_out() :
    print 'Goodbye!'
    main()
'''
def on_get_files() :
    main()
'''
def on_remove_file( filename ) :
    print filename + ' was removed from the directory. '

def list_user_files(user):
    for dirpath, dirnames, filenames in os.walk("~/OneDir_server/%s" %user):
        for f in filenames:
            fp = os.path.join(dirpath,f)
            print fp

def total_size( ) :
    size = 0
    count = 0
    for dirpath, dirnames, filenames in os.walk("~/OneDir_server/"):
        for f in filenames:
            fp = os.path.join(dirpath,f)
            size += os.path.getsize(fp)
            count += 1
    print 'The total size of the directory is %d bytes with %d files' %(size,count)

def user_size( user ) :
    size = 0
    count = 0
    for dirpath, dirnames, filenames in os.walk("~/OneDir_server/%s" % user):
        for f in filenames:
            fp = os.path.join(dirpath,f)
            size += os.path.getsize(fp)
            count +=1
    print 'The total size of %s\'s directory is %d bytes with %d files' %(user,size,count)

def main() :
        y = 0
        admin_code = raw_input('Please enter admin code: ')

        while y != 3 and admin_code != 'cs3240':
            y = y+1
            admin_code = raw_input('Incorrect, please reenter: ')

        if admin_code == 'cs3240':

            pcorrect = false
            
            print 'This is the admin interface of OneDir. Please sign in using your admin username and password.'
            username = raw_input( 'Username: ')
            password = raw_input( 'Password: ')

            if(d.username_available(username) == False):
                if(d.get_info(username)['password'] == password):
                    pcorrect = True
                    print 'You have successfully signed into your OneDir ADMIN account'

            
            while( d.username_available(username) == True or not pcorrect):
                print ('Wrong username or password, please reenter information')
                username = raw_input( 'Username: ')
                password = raw_input( 'Password: ')
                if(d.username_available(username) == False):
                    if(d.get_info(username)['password'] == password):
                        pcorrect = True
                        print 'You have successfully signed into your OneDir ADMIN account'
            while(true):
                #if the username and password link to an admin account, print the rest
                print 'Please enter the number of the command you would like to execute.'
                print '1. View a users profile information.'
                print '2. Look at a list of all the users files in their directory.'
                print '3. Remove a user and their entire directory.'
                print '4. Remove a specific file from a user\'s directory.'
                print '5. View the total size of a users directory.'
                print '6. View the total size of OneDir'
                print '7. Reset a users password.'
                print '8. View the history of connections to the OneDir server.'
                print '0. Log out. '
                #other possible commands: restart server, move files, connect accounts/merge directories

                admin_command = input( "Command: " )

                if admin_command == 1 :
                    user = raw_input( 'Username of the desired profile: ')

                    while d.username_available(user) == True:
                        user = raw_input( 'No such user exists, re-enter username: ')

                    diction = d.get_info(user)

                    print 'Informatin for ' + user + ": "

                    for k, v in diction.iteritems():
                        print str(k) + " : " + str(v)


                if admin_command == 2 :
                    user = raw_input( 'Username of the desired profile: ')
                    list_user_files(user)

                if admin_command == 3 :
                    user = raw_input( 'Username of the user you would like to remove: ')
                    while d.username_available(user) == False:
                        user = raw_input( 'No such user exists, re-enter username: ')
                    d.remove_user(user)
                    print 'User was removed succesfully.'

                if admin_command == 4 :
                    user = raw_input( 'Username of the desired profile: ')
                    while d.username_available(user) == False:
                        user = raw_input( 'No such user exists, re-enter username: ')

                    filename = raw_input( 'File to remove: ')
                    server.remove( user, filename )

                if admin_command == 5 :
                    user = raw_input( 'Username of the desired profile: ')
                    while d.username_available(user) == False:
                        user = raw_input( 'No such user exists, re-enter username: ')
                    user_size(user)

                if admin_command == 6 :
                    total_size()

                if admin_command == 7 :
                    user = raw_input( 'Username that requires a new password: ')
                    while d.username_available(user) == True:
                        user = raw_input( 'No such user exists, re-enter username: ')

                    password = raw_input( 'Enter the new password for this user: ')

                    d.admin_password_change(user, password)

                if admin_command == 8 :
                    server.connection_times()

                if admin_command == 0 :
                    server.log_out()

        elif y == 3:
            print 'Too many incorrect attempts, goodbye.'

if __name__ == '__main__' :
    main()
