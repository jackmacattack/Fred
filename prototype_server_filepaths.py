#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import os                   # Import OS for filepath

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send('Thank you for connecting')
   c.send('2nd test message')

   username = c.recv(1024)
   path = c.recv(1024)
   size = c.recv(1024)
   name = c.recv(1024)     # create the file

   folder = os.path.expanduser(".\%s\%s" %(username,path))
   if not os.path.exists(folder):
      os.makedirs(folder)
   fullpath = os.path.expanduser(".\%s\%s\%s" %(username,path,name))
   
   createFile = open(fullpath,"wb")
   data = c.recv(int(size))
   createFile.write(data)
   createFile.close()
   
   c.close()                # Close the connection
   break

s.close()
