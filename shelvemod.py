import shelve

class DataFile:
    def __init__(self, filename):
        self.data = shelve.open(filename)

    def add_user(self, name, password):
        if (self.data.has_key(name) == False):
            self.data[name] = [password]

    def username_available(self,name):
        if (self.data.has_key(name) == True):
            return False

        else:
            return True


