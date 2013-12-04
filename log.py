import datetime
class Log:
    def __init__(self, log = 'log.log'):
        self.f = open(log,'a')
    def write(self,string):
        s = '[%s] %s'%(datetime.datetime.now(),string)
        self.f.write(s)
    def close(self):
        self.f.close()
