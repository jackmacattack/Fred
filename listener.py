__author__ = 'Jack'


import socket_thread


class Listener:

    def __init__(self, host, port):
        self.s = socket_thread.SocketThread(host, port, self)

    def on_message(self, addr, data):
        raise NotImplementedError( "Should have implemented this" )