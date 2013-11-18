__author__ = 'Jack'


import listener, socket_thread, time, unittest


class TestListener(listener.Listener):

    def __init__(self, test):
        self.test = test

    def on_message(self, addr, data):
        self.test.assertTrue(data == "Love")


class TestSocketThread(unittest.TestCase):

    thread1 = None
    thread2 = None

    def setUp(self):
        self.thread1 = socket_thread.SocketThread("localhost", 12344, TestListener(self))
        self.thread1.start()

        self.thread2 = socket_thread.SocketThread("localhost", 12345, TestListener(self))
        self.thread2.start()

    def test_message(self):
        self.thread1.connect("localhost", 12345)
        self.thread1.send("Love")
        self.thread1.disconnect()

    def test_two_message(self):
        self.thread1.connect("localhost", 12345)
        self.thread2.connect("localhost", 12344)
        self.thread1.send("Love")
        self.thread2.send("Love")
        self.thread1.disconnect()
        self.thread2.disconnect()

    def tearDown(self):
        self.thread1.stop()
        self.thread2.stop()