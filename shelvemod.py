import shelve

class DataFile:

    def __init__(self, filename):
        self.data = shelve.open(filename)

    def add_user(self, name, pword, q, a, file_count):
        if (self.data.has_key(name) == False):
            self.data[name] = {'password': pword, 'question': q, 'answer': a, 'file_count': file_count}

    def username_available(self, name):
        if (self.data.has_key(name) == True):
            return False

        else:
            return True

    def change_password(self, name, oldpassword, answer, newpassword):
        d = self.data[name]
        if d['answer'] == answer:
            if d['password'] == oldpassword:
                d['password'] = newpassword
                self.data[name] = d
                return True

        return False

    def retrieve_password(self, name, answer):
        d = self.data[name]
        if d['answer'] == answer:
            return d['password']

        return False

    def remove_user(self, name):
        del self.data[name]

    def get_info(self, name):
        return self.data[name]