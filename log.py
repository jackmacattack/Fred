import datetime
import os


class Log:
    def __init__(self, log = '~/OneDir_server/log.log'):
        self.f = open(os.path.expanduser(log),'a')
        self.log = log
    def write(self,string):
        s = '[%s] %s'%(datetime.datetime.now(),string)
        self.f.write(s + "\n")
    def save(self):
        self.f.close()
        self.f = open(os.path.expanduser(self.log),'a')
    def close(self):
        self.f.close()
