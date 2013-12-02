__author__ = 'Jack'

import server
import socket

class Stopper:
    
    def __init__(self):
        self.stopping = False
    
    def stop(self):
        self.stopping = True

def run(stopper):
    s = server.Server("localhost", 12344, "test.txt")
    s.start()

    love = True
    try:
        while not stopper.stopping:# and s.on:
            love = not love
    except KeyboardInterrupt:
        print "Stopping Server"
        return
    print "Stopping Server"

if __name__ == '__main__':
    run(Stopper())
