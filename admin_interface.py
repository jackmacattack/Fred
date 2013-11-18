__author__ = 'msstudent'
from shelvemod import DataFile
d = DataFile('test.txt')

def main() :
        y = 0
        admin_code = raw_input('Please enter admin code: ')

        while y != 3 and admin_code != 'cs3240':
            y = y+1
            admin_code = raw_input('Incorrect, please reenter: ')

        if admin_code == 'cs3240':
            print 'This is the admin interface of OneDir. Please sign in using your admin username and password.'
            username = raw_input( 'Username: ')
            password = raw_input( 'Password: ')

            while( d.username_available(username) == True):
                print ('Wrong username or password, please reenter information')
                username = raw_input( 'Username: ')
                password = raw_input( 'Password: ')

            if(d.username_available(username) == False):
                if(d.get_info(username)['password'] == password):
                    print 'You have successfully signed into your OneDir ADMIN account'

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
                #no such function exists in the flat file

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
                #no such function exists in the flat file

            if admin_command == 5 :
                user = raw_input( 'Username of the desired profile: ')
                while d.username_available(user) == False:
                    user = raw_input( 'No such user exists, re-enter username: ')

                #no such function exists in the flat file

            if admin_command == 6 :
                user = raw_input( 'Username of the desired profile: ')
                filename = raw_input( 'Filename: ')
                #no such function exists in the flat file

            if admin_command == 7 :
                #return whole OneDir size
                print 'Size: '
                #no such function exists in the flat file

            if admin_command == 8 :
                #rerturn all the connection times and users - whatever is possible here
                print 'Times: '
                #no such function exists in the flat file

            if admin_command == 9 :
                user = raw_input( 'Username that requires a new password: ')
                while d.username_available(user) == True:
                    user = raw_input( 'No such user exists, re-enter username: ')

                password = raw_input( 'Enter the new password for this user: ')

                d.admin_password_change(user, password)

            if admin_command == 0 :
                print 'Goodbye!'

        elif y == 3:
            print 'Too many incorrect attempts, goodbye.'

if __name__ == '__main__' :
    main()
