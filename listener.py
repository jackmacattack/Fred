__author__ = 'Jack'


class Listener:

    def on_message(self, addr, data):
        raise NotImplementedError( "Should have implemented this" )