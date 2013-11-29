__author__ = 'Jack'

import server
import socket

import socket

print socket.gethostname()

def run():
    s = server.Server("localhost", 12344, "test.txt")
    s.start()

    love = True
    while True:
        love = not love

if __name__ == '__main__':
    run()
