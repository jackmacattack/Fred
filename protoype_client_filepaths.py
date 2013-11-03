#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import os

s = socket.socket()         # Create a socket object
host = socket.gethostname()#"10.0.0.18"#socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))     # print recieved data
print s.recv(1024)
print s.recv(1024)
un = 'username'
pa = 'first\second'
s.send(un)                  #send username
s.send(pa)                  #send filepath
f = 'test.txt'              # file name
size = os.path.getsize(f)
s.send(str(size))
print 'size =',str(size)
s.send(f)
readByte=open(f,"rb")       #read file
data = readByte.read()
readByte.close()

s.send(data)
s.close                     # Close the socket when done
