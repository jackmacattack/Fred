__author__ = 'Jack'

import server

if __name__ == '__main__':
    s = server.Server("localhost", 12344, "test.txt")
    s.start()

    love = True
    while True:
        love = not love