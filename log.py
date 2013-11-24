
class Log:
    def __init__(self, log = 'log.txt'):
        self.f = open(log,'w')
    def write(self,string):
        self.f.write(string)
    def close(self):
        self.f.close()
