__author__ = "Jack"

import client, unittest, socket, thread, time


class TestClient(unittest.TestCase):

    server_test = False

    def server(self):
        s = socket.socket()         # Create a socket object

        #s.settimeout(5)

        host = socket.gethostname() # Get local machine name
        port = 12345                # Reserve a port for your service.

        s.bind((host, port))        # Bind to the port

        s.listen(5)                 # Now wait for client connection.

        self.exit = False
        while not self.exit:
            try:
                c, addr = s.accept()     # Establish connection with client.

                name = c.recv(1024)     # create the file
                print name
                if name[-4:] == ".dat":
                    name = c.recv(1024)

                if name == "Love":
                    self.server_test = True
                    self.exit = True

                c.close()                # Close the connection
            except socket.error:
                pass

        print "Exiting..."
        s.close()
        thread.exit()

    def setUp(self):    #Sets up a test server
        server_test = False

        thread.start_new_thread(self.server, ())
        self.c = client.Client("localhost", 12344)
        self.c.start("localhost", 12345)

    def test_message(self):
        self.c.send_message("Love")

        time.sleep(5)

        self.assertTrue(self.server_test)

    def test_upload(self):
        file = open("testing_temp_123456789876543213531.dat","w")
        file.write("Love")
        file.close()

        self.c.upload("testing_temp_123456789876543213531.dat")

        time.sleep(5)

        self.assertTrue(self.server_test)

    def tearDown(self):
        self.c.stop()
        self.exit = True
        #thread.exit()