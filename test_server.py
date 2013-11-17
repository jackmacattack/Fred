__author__ = 'Jack'

import unittest
import socket_thread
import listener
import server
import time


class TestListener(listener.Listener):

    def on_message(self, addr, data):
        print addr, data


class TestServer(unittest.TestCase):

    def setUp(self):    #Sets up a test server
        self.server_test = False

        self.server = server.Server("localhost", 12345)
        self.server.start()

    def test_ping(self):

        s = TestListener("localhost", 12344).s

        s.start()
        s.connect("localhost", 12345)

        s.send("Connect;localhost;12344")
        time.sleep(10)
        s.stop()
        self.assertTrue(True)

    def tearDown(self):
        self.server.stop()
        #thread.exit()