__author__ = 'msstudent'
from shelvemod import DataFile
import server
import os
import shutil
d = DataFile(os.path.expanduser("~/OneDir_server/db"))

def log_out() :
    print 'Goodbye!'
    main()
'''
def on_get_files() :
    main()
'''
def on_remove_file( filename ) :
    print filename + ' was removed from the directory. '

def list_user_files(user):
    s = os.path.expanduser( "~/OneDir_server/%s" %user ) 
    for dirpath, dirnames, filenames in os.walk(s):
        for f in filenames:
            fp = os.path.join(dirpath,f)
            print fp

def total_size( ) :
    size = 0
    count = 0
    s = os.path.expanduser( "~/OneDir_server/")
    for dirpath, dirnames, filenames in os.walk(s):
        for f in filenames:
            fp = os.path.join(dirpath,f)
            size += os.path.getsize(fp)
            count += 1
    print 'The total size of the directory is %d bytes with %d files' %(size,count)

def user_size( user ) :
    size = 0
    count = 0
    s = os.path.expanduser( "~/OneDir_server/%s" %user )
    for dirpath, dirnames, filenames in os.walk(s):
        for f in filenames:
            fp = os.path.join(dirpath,f)
            size += os.path.getsize(fp)
            count +=1
    print 'The total size of %s\'s directory is %d bytes with %d files' %(user,size,count)

def read_log():# change log name
    count = 0
    for line in reversed(open("log.log").readlines()):
        if count!=0 and count%10 == 0:
            i = raw_input("continue? (y/n)")
            if i == "n":
                break
        print line.rstrip()
        count +=1

def main() :
        y = 0
        admin_code = raw_input('Please enter admin code: ')

        while y != 3 and admin_code != 'cs3240':
            y = y+1
            admin_code = raw_input('Incorrect, please reenter: ')

        if admin_code == 'cs3240':
            print 'You have successfully signed into your OneDir ADMIN account'
            while(True):
                #if the username and password link to an admin account, print the rest
                print 'Please enter the number of the command you would like to execute.'
                print '1. View a users profile information.'
                print '2. Look at a list of all the users files in their directory.'
                print '3. Remove a user.'
                print '4. View the total size of a users directory.'
                print '5. View the total size of OneDir'
                print '6. Reset a users password.'
                print '7. View the history of connections to the OneDir server.'
                print '0. Quit. '
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
                    print 'here'

                if admin_command == 3 :
                    user = raw_input( 'Username of the user you would like to remove: ')
                    while d.username_available(user) == True:
                        user = raw_input( 'No such user exists, re-enter username: ')
                    d.remove_user(user)
		    d.save()
                    print 'User was removed succesfully.'
                    files= raw_input('remove user files? (y/n)')
                    if files=="y":
			s = os.path.expanduser( "~/OneDir_server/%s" %user) 
                        shutil.rmtree(s)

                if admin_command == 4 :
                    user = raw_input( 'Username of the desired profile: ')
                    while d.username_available(user) == True:
                        user = raw_input( 'No such user exists, re-enter username: ')
                    user_size(user)

                if admin_command == 5 :
                    total_size()

                if admin_command == 6 :
                    user = raw_input( 'Username that requires a new password: ')
                    while d.username_available(user) == True:
                        user = raw_input( 'No such user exists, re-enter username: ')

                    password = raw_input( 'Enter the new password for this user: ')

                    d.admin_pword_change(user, password)

                if admin_command == 7 :
                    read_log()

                if admin_command == 0 :
                    log_out()


        elif y == 3:
            print 'Too many incorrect attempts, goodbye.'

if __name__ == '__main__' :
    main()
