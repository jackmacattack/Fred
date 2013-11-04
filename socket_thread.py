__author__ = 'Jack'


import socket, thread


class SocketThread:

    def __init__(self, host, port, l):
        self.s = socket.socket()
        if host == "localhost":
            host = socket.gethostname()
        self.host = host
        self.port = port
        self.l = l
        self.connected = False
        self.exit = False

    def start(self):
        self.exit = False
        thread.start_new_thread(self.listen, ())

    def connect(self, host, port):
        self.s.connect((host, port))      # print recieved data
        self.connected = True

    def listen(self):
        print self.host, self.port
        s = socket.socket()
        s.bind((self.host, self.port))        # Bind to the port

        s.listen(5)                 # Now wait for client connection.

        while not self.exit:
            c, addr = s.accept()     # Establish connection with client.

            data = c.recv(1024)     # create the file

            self.l.on_message(addr, data)

            c.close()                # Close the connection

        thread.exit()

    def send(self, data):
        if self.connected:
            self.s.send(data)
        else:
            print "Not Connected"

    def disconnect(self):
        self.s.close()
        self.connected = False

    def stop(self):
        self.exit = True