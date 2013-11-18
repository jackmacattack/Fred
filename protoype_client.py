#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = "10.0.0.18"#socket.gethostname() # Get local machine name
port = 12344                # Reserve a port for your service.

s.connect((host, port))     # print recieved data
print s.recv(1024)
print s.recv(1024)

f = 'test.txt'              # file name
s.send(f)
readByte=open(f,"rb")       #read file
data = readByte.read()
readByte.close()

s.send(data)
s.close                     # Close the socket when done
