__author__ = 'Jack'

import server
import socket
import os

class Stopper:
    
    def __init__(self):
        self.stopping = False
    
    def stop(self):
        self.stopping = True

def run(stopper):
    folder = os.path.expanduser("~/OneDir_server/")
    if not os.path.exists(folder):                              #check if folder exists
        os.makedirs(folder)
    s = server.Server("172.25.98.24", 12344, folder + "db" )
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
