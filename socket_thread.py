__author__ = 'Jack'


import socket
import thread
import threading


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
        self.t = threading.Thread(name='server', target=self.listen)

    def start(self):
        self.exit = False
        #thread.start_new_thread(self.listen, ())
        self.t.start()

    def connect(self, host, port):

        self.other_host = host
        self.other_port = port

        if host == "localhost":
            host = socket.gethostname()

        self.s.connect((host, port))      # print recieved data
        self.connected = True

    def listen(self):
        try:
            s = socket.socket()

            s.bind((self.host, self.port))        # Bind to the port

            s.listen(5)                 # Now wait for client connection.

            while not self.exit:
                #print "Start Again"
                c, addr = s.accept()     # Establish connection with client.
                #print "Accept"
                data = c.recv(1024)     # create the file

                c.close()                # Close the connection

                if data:
                    self.l.on_message(addr, data)

            s.close()
            #thread.exit()

        except Exception:
            print "Trace..."
            import traceback
            print traceback.format_exc()

    def send(self, data):
        if self.connected:
            self.s.send(data)

            self.reset()
        else:
            print "Not Connected. Message: ", data, " not sent."

    def reset(self):
        self.disconnect()
        self.connect(self.other_host, self.other_port)

    def disconnect(self):
        self.s.close()
        self.connected = False
        self.s = socket.socket()

    def stop(self):
        self.exit = True

        try:
            self.connect(self.host, self.port)
            self.disconnect()
        except socket.error:
            pass
