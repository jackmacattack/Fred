__author__ = 'Jack'


import connector, unittest, socket, thread, time


class TestClient(unittest.TestCase):

    connector1 = None
    connector2 = None

    def setUp(self):
        self.connector1 = connector.Connector()
        self.connector2 = connector.Connector()

    def test_connect(self):
        self.connector2.start()
        self.connector1.connect()