__author__ = 'Jack'

import socket               # Import socket module

class Client:

	def __init__(self):
		host = "10.0.0.18"#socket.gethostname() # Get local machine name
		port = 12344                # Reserve a port for your service.

	def upload(self, file_name):
		s = socket.socket()         # Create a socket object

		s.connect((host, port))     # print recieved data

		s.send(f)
		readByte=open(file_name,"rb")       #read file
		data = readByte.read()
		readByte.close()

		s.send(data)
		s.close                     # Close the socket when done
		
	def send_message(self, message): 
		s = socket.socket()         # Create a socket object

		s.connect((host, port))     # print recieved data

		s.send(message)

		s.close                     # Close the socket when done
		

